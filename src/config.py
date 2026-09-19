from string import Template

import yaml


class Config:
    def __init__(
        self,
        bot_token: str,
        welcome_channel_id: int | None,
        welcome_message: str | None,
        masked_role_id: int | None,
        masked_channel_id: int | None,
        masked_message: str | None,
    ):
        self._bot_token = bot_token
        self._welcome_channel_id = welcome_channel_id
        self._welcome_message_str = welcome_message
        self._masked_role_id = masked_role_id
        self._masked_channel_id = masked_channel_id
        self._masked_message_str = masked_message

    @property
    def bot_token(self) -> str:
        return self._bot_token

    @property
    def welcome_channel_id(self) -> int | None:
        return self._welcome_channel_id

    @property
    def welcome_message(self) -> Template | None:
        if self._welcome_message_str:
            self._welcome_message = Template(self._welcome_message_str)

            return self._welcome_message

        return None

    @property
    def masked_role_id(self) -> int | None:
        return self._masked_role_id

    @property
    def masked_channel_id(self) -> int | None:
        return self._masked_channel_id

    @property
    def masked_message(self) -> Template | None:
        if self._masked_message_str:
            self._masked_message = Template(self._masked_message_str)

            return self._masked_message

        return None

    @classmethod
    def from_yaml(cls, path: str | None = None):
        if not path:
            path = "./config.yaml"

        with open(path) as file:
            config: dict = yaml.safe_load(file)

            return cls(
                bot_token=config["bot_token"],
                welcome_channel_id=config.get("on_join", {}).get("channel_id")
                if config.get("on_join")
                else None,
                welcome_message=config.get("on_join", {}).get("message")
                if config.get("on_join")
                else None,
                masked_role_id=config.get("on_role_added", {}).get("role_id")
                if config.get("on_role_added")
                else None,
                masked_channel_id=config.get("on_role_added", {}).get("channel_id")
                if config.get("on_role_added")
                else None,
                masked_message=config.get("on_role_added", {}).get("message")
                if config.get("on_role_added")
                else None,
            )
