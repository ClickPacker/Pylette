from typing import Final, Union, Optional, List, NoReturn
from dataclasses import dataclass, field
from patterns.filters import *

__all__ = [
    "CreateStyle",
    "ErrorMessage",
    "WarningMessage",
    "SuccessMessage",
    "WaitMessage",
]


@dataclass
class CreateStyle:
    """
    Pattern-style for creating style
    """
    message: Optional[Union[str, int, list, dict, tuple, float]] = None
    ansi_character: str = "\033"
    style_modifiers: Optional[List[Union[str, int]]] = field(default_factory=lambda: None)
    text_color: Optional[Union[str, int]] = None
    background_color: Optional[Union[str, int]] = None
    indent: Optional[bool] = None

    def __setattr__(self, key, value) -> NoReturn:
        """
        Post-initialization of passed arguments with validation of certain specified values
        """
        if key in ["message", "ansi_character", "style_modifiers", "text_color", "background_color", "indent"]:
            if value:
                if key == "message":
                    self.__dict__[key] = value
                elif key == "ansi_character":
                    self.__dict__[key] = value
                elif key == "indent" and value:
                    self.message = f" {self.message} "
                    self.__dict__[key] = value
                elif key == "style_modifiers":
                    self.__dict__[key] = _validate_modifiers(list(map(str, value)))
                elif key == "text_color":
                    self.__dict__[key] = _validate_color_text(str(value))
                elif key == "background_color":
                    self.__dict__[key] = _validate_color_back(str(value))
            else:
                self.__dict__[key] = None
        else:
            raise TypeError("It is not possible to add an unnamed variable inside the class")

    def __tag_constructor(self) -> str:
        """
        Method builds tag from self.ansi_character, self.style_modifiers, self.text_color, self.background_color
        :return: Tag is assembled in the form of "ANSI[ARGSm"
        """
        if self.style_modifiers is self.text_color is self.background_color is None:
            final_tag = f"{self.ansi_character}[0m"
        else:
            means = []
            if self.style_modifiers:
                means.extend(self.style_modifiers)
            if self.text_color:
                means.append(self.text_color)
            if self.background_color:
                means.append(self.background_color)
            args = ";".join(map(str, means))
            final_tag = "{ansi_character}[{args}m".format(ansi_character=self.ansi_character, args=args)
        return final_tag

    def print_message(self, message):
        """
        Prints a styled message
        :param message: The message to be printed. Defaults to None.
        :return: The styled message as a string.
        """
        return self.__str__(message=message)

    def __str__(self, *args, **kwargs) -> str:
        return "{open_tag}{message}{close_tag}".format(
                        open_tag=self.__tag_constructor(),
                        message=kwargs["message"] if kwargs else self.message,
                        close_tag=f"{self.ansi_character}[0m")


@dataclass
class ErrorMessage(CreateStyle):
    """
    Стиль для сообщения об ошибке
    """
    style_modifiers: Final[List[Union[str, int]]] = field(default_factory=lambda: [3])
    text_color: Final[Union[str, int]] = 31


@dataclass
class WarningMessage(CreateStyle):
    """
    Стиль для сообщения-предупреждения
    """
    style_modifiers: Final[List[Union[str, int]]] = field(default_factory=lambda: [4])
    text_color: Final[Union[str, int]] = 33


@dataclass
class SuccessMessage(CreateStyle):
    """
    Стиль для сообщения об успешном выполнении операции
    """
    style_modifiers: Final[List[Union[str, int]]] = field(default_factory=lambda: [1])
    text_color: Final[Union[str, int]] = 32


@dataclass
class WaitMessage(CreateStyle):
    """
    Стиль для сообщения об успешном подключении
    """
    style_modifiers: Final[List[Union[str, int]]] = field(default_factory=lambda: [])
    text_color: Final[Union[str, int]] = 36

@dataclass
class HighLighting(CreateStyle):
    """
    Родительский класс для всех хайлайтингов
    """
    indent: bool = True
    style_modifiers: Final[List[Union[str, int]]] = field(default_factory=lambda: [3])
    text_color: Union[str, int]
    background_color: Union[str, int]
@dataclass
class GreenHighlighting(HighLighting):
    """
    Стиль для зеленого выделения
    """
    text_color: Final[Union[str, int]] = 30
    background_color: Final[Union[str, int]] = 42

@dataclass
class RedHighlighting(HighLighting):
    """
    Стиль для красного выделения
    """
    text_color: Final[Union[str, int]] = 30
    background_color: Final[Union[str, int]] = 41

@dataclass
class YellowHighlighting(HighLighting):
    """
    Стиль для желтого выделения
    """
    text_color: Final[Union[str, int]] = 30
    background_color: Final[Union[str, int]] = 43