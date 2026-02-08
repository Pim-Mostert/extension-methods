# %%

from typing import Callable, Concatenate, cast


class Extension[TIn, **P, TOut]:
    def __init__(
        self,
        func: Callable[Concatenate[TIn, P], TOut],
        *args: P.args,
        **kwargs: P.kwargs,
    ):
        self._func = func
        self._args = args
        self._kwargs = kwargs

    def __call__(
        self,
        other: TIn,
        *args: P.args,
        **kwargs: P.kwargs,
    ) -> TOut:
        return self._func(other, *args, **kwargs)

    def __ror__(self, other: TIn) -> TOut:
        return self._func(other, *self._args, **self._kwargs)


def extension[TIn, **P, TOut](
    func: Callable[Concatenate[TIn, P], TOut],
):
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> Extension[TIn, P, TOut]:
        return Extension(func, *args, **kwargs)

    return cast(Callable[P, TOut], wrapper)


@extension
def multiply(source: int, factor: int) -> int:
    """
    moi
    """
    return factor * source


result = 7 | multiply(3)

result
