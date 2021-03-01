# -*- coding: utf-8 -*-
"""Direct current electromagnetics

    This package contains tools, modelling operators, and managers for:

    * Electrical Resistivity Tomography (ERT) / Induced polarization (IP)
    * Vertical Electric Sounding (VES)
"""

import pygimli as pg
from .ert import (simulate, estimateError,
                  createGeometricFactors, createInversionMesh)
from .ertManager import ERTManager
from .ertModelling import ERTModelling, ERTModellingReference
from .ertScheme import createData
from .ves import VESModelling, VESCModelling, VESManager

from .visualization import showERTData
from .importData import load

show = showERTData
geometricFactor = pg.core.geometricFactor
geometricFactors = geometricFactor
