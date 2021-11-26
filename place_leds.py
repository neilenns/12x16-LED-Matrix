import sys
# This script automates renumbering the references on a grid
# of LEDs. 
import re
from pcbnew import *

filename="12x16-LED-Matrix.kicad_pcb"

pcb = LoadBoard(filename)
for module in pcb.GetModules():
  if re.search("^D", module.GetReference()):
    # module.Reference().SetVisible(False)
    module.SetLayer(layertable["F.Fab"])
    print("* Module: %s"%module.GetReference())
pcb.Save(filename)

