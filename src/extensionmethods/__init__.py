from importlib.metadata import PackageNotFoundError, version

from .extensions import extension

try:
    __version__ = version("extensionmethods")
except PackageNotFoundError:
    __version__ = "noinstall"

__all__ = [
    "extension",
]
