import sys
# This script automates renumbering the references on a grid
# of LEDs. 
import re
from pcbnew import *

filename="12x16-LED-Matrix.kicad_pcb"

pcb = LoadBoard(filename)

def get_layertable():
    layertable = {}
    numlayers = PCB_LAYER_ID_COUNT
    for i in range(numlayers):
        layertable[pcb.GetLayerName(i)] = i
    return layertable

layertable = get_layertable()

for module in pcb.GetModules():
  if re.search("^D", module.GetReference()):
    # module.Reference().SetVisible(False)
    module.Reference().SetLayer(layertable["F.Fab"])
    print("* Module: %s"%module.GetReference())
pcb.Save(filename)

