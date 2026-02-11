from typing import Callable, Concatenate


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

    def __ror__(self, other: TIn) -> TOut:
        return self._func(other, *self._args, **self._kwargs)


def extension[TIn, **P, TOut](
    func: Callable[Concatenate[TIn, P], TOut],
):
    def extension_factory(*args: P.args, **kwargs: P.kwargs) -> Extension[TIn, P, TOut]:
        return Extension(func, *args, **kwargs)

    return extension_factory
