from typing import Protocol, runtime_checkable


class SupportPrint(Protocol):
    def print(self, arg: str) -> None:
        pass

class SupportWrite(Protocol):
    def write(self, arg: str) -> None:
        pass

class Anything:
    logger: SupportPrint
    def __init__(self, logger: SupportPrint) -> None:
        logger.print(__name__)


class StdPrintabe:
    def print(self, arg: str) -> None:
        print(f"printing: {arg}")

    def other_methos(self) -> None:
        pass

class NonComplientWithPrintable:
    def print(self, arg: int) -> None:
        print(f"printing: {arg}")



Anything(StdPrintabe())

# it will break because arg of print method is int type, not str as Printable protocol requires 
# Anything(NonComplientWithPrintable())


# this protocal inherit and merge SupportPrint and SupportWrite and have a buffer property in your definition too
class IO(SupportPrint, SupportWrite, Protocol):
    buffer: str
    pass

class IOWrapper:
    io: IO
    def __init__(self, io: IO) -> None:
        io.print(__name__)
        io.write(__name__)

class StdPrintAndWrire:
    buffer: str
    def print(self, arg: str) -> None:
        print(f"printing: {arg}")

    def write(self, arg: str) -> None:
        print(f"writing: {arg}")


print(
    IOWrapper(StdPrintAndWrire())
)

# runtime checkable
@runtime_checkable
class IOCheckable(IO, Protocol):
    pass

intance = StdPrintAndWrire()

print(
    "is instance o IOCheckable",
    isinstance(intance, IOCheckable)
)