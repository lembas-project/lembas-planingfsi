"""Lembas plugin for planingfsi hydrodynamic simulations."""

from lembas_planingfsi._version import __version__
from lembas_planingfsi.flat_plate import PlaningPlateCase

__all__ = ["PlaningPlateCase", "Plugin", "__version__"]


class Plugin:
    """Lembas plugin registration."""

    name = "lembas-planingfsi"
    version = __version__
    case_handlers = [PlaningPlateCase]
