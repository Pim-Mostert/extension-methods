# %%

from typing import Callable, Generic, TypeVar

TIn = TypeVar("TIn")
TOut = TypeVar("TOut")


class Extension(Generic[TIn, TOut]):
    def __init__(self, func: Callable[[TIn], TOut]):
        self._func = func

    def __ror__(self, other: TIn) -> TOut:
        return self._func(other)


def extension(func: Callable[[TIn], TOut]) -> Extension[TIn, TOut]:
    return Extension[TIn, TOut](func)


@extension
def double(x: int) -> int:
    """
    moi
    """
    return 2 * x


result = 7 | double

print(result)
