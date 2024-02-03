from dataclasses import dataclass
from typing import TypedDict, Union, List

__all__ = [
    "_validate_modifiers",
    "_validate_color_text",
    "_validate_color_back"
]


@dataclass
class __FilterColors(TypedDict):
    black: int
    red: int
    green: int
    yellow: int
    blue: int
    purple: int
    cyan: int
    white: int


@dataclass
class __FilterModifiers(TypedDict):
    bold: int
    faded: int
    cursive: int
    underlined: int
    blink: int
    strikeout: int


filter_text = __FilterColors(
    black=30,
    red=31,
    green=32,
    yellow=33,
    blue=34,
    purple=35,
    cyan=36,
    white=37
)

filter_back = __FilterColors(
    black=40,
    red=41,
    green=42,
    yellow=43,
    blue=44,
    purple=45,
    cyan=46,
    white=47
)

filter_modifiers = __FilterModifiers(
    bold=1,
    faded=2,
    cursive=3,
    underlined=4,
    blink=5,
    strikeout=9
)


def _validate_color_text(value: str) -> Union[int, None]:
    """
    Валидирует значения цвета текста и позволяет преобразовать их в читаемый вид
    :param value: любое значение типа str
    :return: возвращает читаемое значение для форматирования строки в промежутке от 30 до 37
    """
    if value in filter_text.keys():
        return filter_text[value]
    elif "30" <= value <= "37":
        return int(value)
    return None


def _validate_color_back(value: str) -> Union[int, None]:
    """
    Валидирует значения цвета фона и позволяет преобразовать их в читаемый вид
    :param value: любое значение типа str
    :return: возвращает читаемое значение для форматирования строки в промежутке от 40 до 47
    """
    if value in filter_back.keys():
        return filter_back[value]
    elif "40" <= value <= "47":
        return int(value)
    return None


def _validate_modifiers(values: List[str]) -> Union[List[int], None]:
    """
    Валидирует список значений модификаторов шрифта и позволяет преобразовать их в читаемый вид
    :param values: любое значение типа str
    :return: возвращает читаемое значение для форматирования строки в промежутке от 1 до 5 и 9
    """
    means = []
    for value in values:
        if value in filter_modifiers.keys():
            means.append(filter_modifiers[value])
        elif value in ['1', '2', '3', '4', '5', '9']:
            means.append(value)
    return means if means else None
