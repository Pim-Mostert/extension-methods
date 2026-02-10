from typing import Callable, Concatenate, Type, cast


class Extension[TIn, **P, TOut]:
    def __init__(
        self,
        to: Type[TIn],
        func: Callable[Concatenate[TIn, P], TOut],
        *args: P.args,
        **kwargs: P.kwargs,
    ):
        self._func = func
        self._to = to
        self._args = args
        self._kwargs = kwargs

    def __ror__(self, other: TIn) -> TOut:
        if not isinstance(other, self._to):
            raise TypeError(
                f"Extension '{self._func.__name__}' can only be used on '{self._to.__name__}', "
                f"not '{type(other).__name__}'"
            )

        return self._func(other, *self._args, **self._kwargs)


def extension[TIn](to: Type[TIn]):
    def wrapper[**P, TOut](
        func: Callable[Concatenate[TIn, P], TOut],
    ):
        def extension_factory(
            *args: P.args, **kwargs: P.kwargs
        ) -> Extension[TIn, P, TOut]:
            return Extension(to, func, *args, **kwargs)

        return cast(Callable[P, TOut], extension_factory)

    return wrapper
