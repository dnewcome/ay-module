#!/usr/bin/env python3
"""Generate ay_module.kicad_sch from circuit modules."""

import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from lib_symbols import get_lib_symbols
from circuit_power_midi import get_power_midi_elements
from circuit_ay_arduino_cv_audio import get_main_circuit_elements

HEADER = """(kicad_sch
  (version 20231120)
  (generator "python-generator")
  (generator_version "1.0")
  (paper "A2")
  (title_block
    (title "AY-3-8910 Eurorack Module")
    (rev "0.1")
    (company "DIY")
  )
"""

FOOTER = ")\n"


def build_schematic() -> str:
    parts = []
    parts.append(HEADER)

    # Lib symbols block
    parts.append("  (lib_symbols\n")
    parts.append(get_lib_symbols())
    parts.append("  )\n\n")

    # Circuit elements
    parts.append(get_power_midi_elements())
    parts.append("\n")
    parts.append(get_main_circuit_elements())
    parts.append("\n")

    parts.append(FOOTER)
    return "".join(parts)


if __name__ == "__main__":
    output_path = os.path.join(os.path.dirname(__file__), "ay_module.kicad_sch")
    print("Building schematic...")
    sch = build_schematic()
    with open(output_path, "w") as f:
        f.write(sch)
    print(f"Written: {output_path} ({len(sch):,} bytes)")
