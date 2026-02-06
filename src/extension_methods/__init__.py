from importlib.metadata import PackageNotFoundError, version

from .extensions import *  # noqa: F403

try:
    __version__ = version("extension_methods")
except PackageNotFoundError:
    __version__ = "noinstall"
