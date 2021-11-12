import sys
# This script automates renumbering the references on a grid
# of LEDs. 
import re
from pcbnew import *

filename="12x16-LED-Matrix.kicad_pcb"

pcb = LoadBoard(filename)
i = 16*12
for module in pcb.GetModules():
  if re.search("^D", module.GetReference()):
    module.SetReference("D%d"%i)
    module.Reference().SetVisible(False)
    print("* Module: %s"%module.GetReference())
    i-=1
pcb.Save(filename)

