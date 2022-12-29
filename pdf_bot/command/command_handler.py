from telegram.ext import BaseHandler
from telegram.ext import CommandHandler as TelegramCommandHandler
from telegram.ext import filters

from pdf_bot.telegram_handler import AbstractTelegramHandler

from .command_service import CommandService


class CommandHandler(AbstractTelegramHandler):
    _START_COMMAND = "start"
    _HELP_COMMAND = "help"
    _SEND_COMMAND = "send"

    def __init__(self, command_service: CommandService, admin_telegram_id: int) -> None:
        self.command_service = command_service
        self.admin_telegram_id = admin_telegram_id

    @property
    def handlers(self) -> list[BaseHandler]:
        return [
            TelegramCommandHandler(
                self._START_COMMAND, self.command_service.send_start_message
            ),
            TelegramCommandHandler(
                self._HELP_COMMAND, self.command_service.send_help_message
            ),
            TelegramCommandHandler(
                self._SEND_COMMAND,
                self.command_service.send_message_to_user,
                filters.User(self.admin_telegram_id),
            ),
        ]
