from typing import Dict, List

from smart_donkey._defaults import DEFAULT_SYSTEM_MESSAGE
from smart_donkey.db.models import Message


def stringify_attributes(obj):
    attributes = vars(obj)

    return ", ".join(f"{key}: {value}" for key, value in attributes.items())


def format_messages(messages: List[Message], instruction: str) -> List[Dict[str, str]]:
    final_messages: List[Dict[str, str]] = list()
    final_messages.append({"role": "system", "content": DEFAULT_SYSTEM_MESSAGE.format(instruction)})

    for message in messages:
        message_dict = {"role": message.role, "content": message.content}

        final_messages.append(message_dict)

    return list(reversed(final_messages))

