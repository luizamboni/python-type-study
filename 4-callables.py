from typing import Callable, Any, TypeVar

MathOp = Callable[[float, float], float]

def run_op(f: MathOp, a: float, b: float) -> Any:
    return f(a,b)

def multiplice(a: float, b: float) -> float:
    return a*b 

def sum(a: float, b: float) -> float:
    return a+b

print(
    run_op(multiplice, 1,2)
)

print(
    run_op(sum, 1,2)
)

print(
    run_op(lambda a,b: a **b, 1,2)
)


class WrapperOp:
    op: Callable[['WrapperOp', float, float], float]

    def __init__(self, op: MathOp) -> None:
        ## ignore this line because
        ## when op is assigned it is turned a method 
        ## and typehint alert the diff between argment and property (self presence)
        self.op = op # type: ignore

    def run(self, a: float, b: float) -> float:
        return self.op(a, b)

wrap = WrapperOp(sum)

print(
    wrap.run(1, 10)
)