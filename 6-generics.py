from typing import Generic, TypeVar, Union

T = TypeVar('T')

class Logger(Generic[T]):

    def print_with_dots(self, arg: T):
        print(f"....{arg}")


logger_str:Logger[str] = Logger()

# logger.print_with_dots(154) # this will break because logger type Generic was defined as str

logger_str.print_with_dots('154')

logger_int:Logger[int] = Logger()
logger_int.print_with_dots(154)


logger: Logger[Union[int, str]] = Logger()

logger.print_with_dots('asdfasd')
logger.print_with_dots(1)
