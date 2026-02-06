from importlib.metadata import PackageNotFoundError, version

from .extensions import *  # noqa: F403

try:
    __version__ = version("extensionmethods")
except PackageNotFoundError:
    __version__ = "noinstall"
