def get_lib_symbols() -> str:
    parts = []

    # -------------------------------------------------------------------------
    # Symbol 1: Custom:AY-3-8910  (40-pin DIP)
    # -------------------------------------------------------------------------
    ay_left_pins = [
        (1,  "GND",      "power_in"),
        (2,  "NC",       "no_connect"),
        (3,  "AoutB",    "output"),
        (4,  "AoutA",    "output"),
        (5,  "NC",       "no_connect"),
        (6,  "IOB7",     "bidirectional"),
        (7,  "IOB6",     "bidirectional"),
        (8,  "IOB5",     "bidirectional"),
        (9,  "IOB4",     "bidirectional"),
        (10, "IOB3",     "bidirectional"),
        (11, "IOB2",     "bidirectional"),
        (12, "IOB1",     "bidirectional"),
        (13, "IOB0",     "bidirectional"),
        (14, "IOA7",     "bidirectional"),
        (15, "IOA6",     "bidirectional"),
        (16, "IOA5",     "bidirectional"),
        (17, "IOA4",     "bidirectional"),
        (18, "IOA3",     "bidirectional"),
        (19, "IOA2",     "bidirectional"),
        (20, "IOA1",     "bidirectional"),
    ]
    ay_right_pins = [
        (21, "IOA0",     "bidirectional"),
        (22, "CLOCK",    "input"),
        (23, "~{RESET}", "input"),
        (24, "A9",       "input"),
        (25, "A8",       "input"),
        (26, "TEST2",    "no_connect"),
        (27, "BDIR",     "input"),
        (28, "BC2",      "input"),
        (29, "BC1",      "input"),
        (30, "DA7",      "bidirectional"),
        (31, "DA6",      "bidirectional"),
        (32, "DA5",      "bidirectional"),
        (33, "DA4",      "bidirectional"),
        (34, "DA3",      "bidirectional"),
        (35, "DA2",      "bidirectional"),
        (36, "DA1",      "bidirectional"),
        (37, "DA0",      "bidirectional"),
        (38, "AoutC",    "output"),
        (39, "TEST1",    "no_connect"),
        (40, "VCC",      "power_in"),
    ]

    ay_pin_lines = []
    for (n, name, ptype) in ay_left_pins:
        y = round(24.13 - (n - 1) * 2.54, 6)
        ay_pin_lines.append(
            f'    (pin {ptype} line (at -12.7 {y} 0) (length 2.54)\n'
            f'      (name "{name}" (effects (font (size 1.27 1.27))))\n'
            f'      (number "{n}" (effects (font (size 1.27 1.27)))))'
        )
    for (n, name, ptype) in ay_right_pins:
        y = round(24.13 - (40 - n) * 2.54, 6)
        ay_pin_lines.append(
            f'    (pin {ptype} line (at 12.7 {y} 180) (length 2.54)\n'
            f'      (name "{name}" (effects (font (size 1.27 1.27))))\n'
            f'      (number "{n}" (effects (font (size 1.27 1.27)))))'
        )

    parts.append(
        '  (symbol "Custom:AY-3-8910" (pin_numbers (hide yes)) (pin_names (offset 1.016))\n'
        '    (property "Reference" "U" (at 0 27.94 0) (effects (font (size 1.27 1.27))))\n'
        '    (property "Value" "AY-3-8910" (at 0 30.48 0) (effects (font (size 1.27 1.27))))\n'
        '    (property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) (hide yes)))\n'
        '    (property "Datasheet" "~" (at 0 0 0) (effects (font (size 1.27 1.27)) (hide yes)))\n'
        '    (symbol "AY-3-8910_0_1"\n'
        '      (rectangle (start -10.16 -25.4) (end 10.16 25.4))\n'
        '    )\n'
        '    (symbol "AY-3-8910_1_1"\n'
        + "\n".join(ay_pin_lines) + "\n"
        '    )\n'
        '  )'
    )

    # -------------------------------------------------------------------------
    # Symbol 2: Custom:Arduino_ProMicro
    # -------------------------------------------------------------------------
    pm_left_pins = [
        (1,  "TX",       "output"),
        (2,  "RX",       "input"),
        (3,  "GND",      "power_in"),
        (4,  "GND",      "power_in"),
        (5,  "D2",       "bidirectional"),
        (6,  "D3",       "bidirectional"),
        (7,  "D4",       "bidirectional"),
        (8,  "D5",       "bidirectional"),
        (9,  "D6",       "bidirectional"),
        (10, "D7",       "bidirectional"),
        (11, "D8",       "bidirectional"),
        (12, "D9",       "bidirectional"),
    ]
    pm_right_pins = [
        (13, "RAW",      "power_in"),
        (14, "GND",      "power_in"),
        (15, "~{RESET}", "input"),
        (16, "VCC",      "power_in"),
        (17, "A3",       "bidirectional"),
        (18, "A2",       "bidirectional"),
        (19, "A1",       "bidirectional"),
        (20, "A0",       "bidirectional"),
        (21, "SCK",      "bidirectional"),
        (22, "MOSI",     "bidirectional"),
        (23, "MISO",     "bidirectional"),
        (24, "D10",      "bidirectional"),
    ]

    pm_pin_lines = []
    for i, (n, name, ptype) in enumerate(pm_left_pins):
        y = round(13.97 - i * 2.54, 6)
        pm_pin_lines.append(
            f'    (pin {ptype} line (at -12.7 {y} 0) (length 2.54)\n'
            f'      (name "{name}" (effects (font (size 1.27 1.27))))\n'
            f'      (number "{n}" (effects (font (size 1.27 1.27)))))'
        )
    for i, (n, name, ptype) in enumerate(pm_right_pins):
        y = round(13.97 - i * 2.54, 6)
        pm_pin_lines.append(
            f'    (pin {ptype} line (at 12.7 {y} 180) (length 2.54)\n'
            f'      (name "{name}" (effects (font (size 1.27 1.27))))\n'
            f'      (number "{n}" (effects (font (size 1.27 1.27)))))'
        )

    parts.append(
        '  (symbol "Custom:Arduino_ProMicro" (pin_numbers (hide yes)) (pin_names (offset 1.016))\n'
        '    (property "Reference" "U" (at 0 19.05 0) (effects (font (size 1.27 1.27))))\n'
        '    (property "Value" "Arduino_ProMicro" (at 0 21.59 0) (effects (font (size 1.27 1.27))))\n'
        '    (property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) (hide yes)))\n'
        '    (property "Datasheet" "~" (at 0 0 0) (effects (font (size 1.27 1.27)) (hide yes)))\n'
        '    (symbol "Arduino_ProMicro_0_1"\n'
        '      (rectangle (start -10.16 -16.51) (end 10.16 16.51))\n'
        '    )\n'
        '    (symbol "Arduino_ProMicro_1_1"\n'
        + "\n".join(pm_pin_lines) + "\n"
        '    )\n'
        '  )'
    )

    # -------------------------------------------------------------------------
    # Symbol 3: Device:R
    # -------------------------------------------------------------------------
    parts.append(
        '  (symbol "Device:R" (pin_numbers (hide yes)) (pin_names (offset 0))\n'
        '    (property "Reference" "R" (at 2.032 0 90) (effects (font (size 1.27 1.27))))\n'
        '    (property "Value" "R" (at 0 0 90) (effects (font (size 1.27 1.27))))\n'
        '    (property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) (hide yes)))\n'
        '    (property "Datasheet" "~" (at 0 0 0) (effects (font (size 1.27 1.27)) (hide yes)))\n'
        '    (symbol "R_0_1"\n'
        '      (rectangle (start -1.016 -2.54) (end 1.016 2.54))\n'
        '    )\n'
        '    (symbol "R_1_1"\n'
        '      (pin passive line (at 0 3.81 270) (length 1.27)\n'
        '        (name "~" (effects (font (size 1.27 1.27))))\n'
        '        (number "1" (effects (font (size 1.27 1.27)))))\n'
        '      (pin passive line (at 0 -3.81 90) (length 1.27)\n'
        '        (name "~" (effects (font (size 1.27 1.27))))\n'
        '        (number "2" (effects (font (size 1.27 1.27)))))\n'
        '    )\n'
        '  )'
    )

    # -------------------------------------------------------------------------
    # Symbol 4: Device:C
    # -------------------------------------------------------------------------
    parts.append(
        '  (symbol "Device:C" (pin_numbers (hide yes)) (pin_names (offset 0.254))\n'
        '    (property "Reference" "C" (at 1.651 0 90) (effects (font (size 1.27 1.27))))\n'
        '    (property "Value" "C" (at 0 0 90) (effects (font (size 1.27 1.27))))\n'
        '    (property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) (hide yes)))\n'
        '    (property "Datasheet" "~" (at 0 0 0) (effects (font (size 1.27 1.27)) (hide yes)))\n'
        '    (symbol "C_0_1"\n'
        '      (polyline (pts (xy -2.032 0) (xy 2.032 0)) (stroke (width 0.508) (type default)) (fill (type none)))\n'
        '      (polyline (pts (xy -2.032 -0.508) (xy 2.032 -0.508)) (stroke (width 0.508) (type default)) (fill (type none)))\n'
        '    )\n'
        '    (symbol "C_1_1"\n'
        '      (pin passive line (at 0 2.54 270) (length 2.54)\n'
        '        (name "~" (effects (font (size 1.27 1.27))))\n'
        '        (number "1" (effects (font (size 1.27 1.27)))))\n'
        '      (pin passive line (at 0 -2.54 90) (length 2.54)\n'
        '        (name "~" (effects (font (size 1.27 1.27))))\n'
        '        (number "2" (effects (font (size 1.27 1.27)))))\n'
        '    )\n'
        '  )'
    )

    # -------------------------------------------------------------------------
    # Symbol 5: Device:C_Polarized
    # -------------------------------------------------------------------------
    parts.append(
        '  (symbol "Device:C_Polarized" (pin_numbers (hide yes)) (pin_names (offset 0.254))\n'
        '    (property "Reference" "C" (at 1.651 0 90) (effects (font (size 1.27 1.27))))\n'
        '    (property "Value" "C_Polarized" (at 0 0 90) (effects (font (size 1.27 1.27))))\n'
        '    (property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) (hide yes)))\n'
        '    (property "Datasheet" "~" (at 0 0 0) (effects (font (size 1.27 1.27)) (hide yes)))\n'
        '    (symbol "C_Polarized_0_1"\n'
        '      (polyline (pts (xy -2.032 0) (xy 2.032 0)) (stroke (width 0.508) (type default)) (fill (type none)))\n'
        '      (polyline (pts (xy -2.032 -0.508) (xy 2.032 -0.508)) (stroke (width 0.508) (type default)) (fill (type none)))\n'
        '      (text "+" (at -1.524 1.524 0) (effects (font (size 1.27 1.27))))\n'
        '    )\n'
        '    (symbol "C_Polarized_1_1"\n'
        '      (pin passive line (at 0 2.54 270) (length 2.54)\n'
        '        (name "+" (effects (font (size 1.27 1.27))))\n'
        '        (number "1" (effects (font (size 1.27 1.27)))))\n'
        '      (pin passive line (at 0 -2.54 90) (length 2.54)\n'
        '        (name "~" (effects (font (size 1.27 1.27))))\n'
        '        (number "2" (effects (font (size 1.27 1.27)))))\n'
        '    )\n'
        '  )'
    )

    # -------------------------------------------------------------------------
    # Symbol 6: Device:D
    # -------------------------------------------------------------------------
    parts.append(
        '  (symbol "Device:D" (pin_numbers (hide yes)) (pin_names (offset 0))\n'
        '    (property "Reference" "D" (at 0 2.54 0) (effects (font (size 1.27 1.27))))\n'
        '    (property "Value" "D" (at 0 -2.54 0) (effects (font (size 1.27 1.27))))\n'
        '    (property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) (hide yes)))\n'
        '    (property "Datasheet" "~" (at 0 0 0) (effects (font (size 1.27 1.27)) (hide yes)))\n'
        '    (symbol "D_0_1"\n'
        '      (rectangle (start -0.762 -1.016) (end 0.762 1.016))\n'
        '    )\n'
        '    (symbol "D_1_1"\n'
        '      (pin passive line (at -2.54 0 0) (length 2.54)\n'
        '        (name "K" (effects (font (size 1.27 1.27))))\n'
        '        (number "1" (effects (font (size 1.27 1.27)))))\n'
        '      (pin passive line (at 2.54 0 180) (length 2.54)\n'
        '        (name "A" (effects (font (size 1.27 1.27))))\n'
        '        (number "2" (effects (font (size 1.27 1.27)))))\n'
        '    )\n'
        '  )'
    )

    # -------------------------------------------------------------------------
    # Symbol 7: Device:D_Schottky
    # -------------------------------------------------------------------------
    parts.append(
        '  (symbol "Device:D_Schottky" (pin_numbers (hide yes)) (pin_names (offset 0))\n'
        '    (property "Reference" "D" (at 0 2.54 0) (effects (font (size 1.27 1.27))))\n'
        '    (property "Value" "D_Schottky" (at 0 -2.54 0) (effects (font (size 1.27 1.27))))\n'
        '    (property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) (hide yes)))\n'
        '    (property "Datasheet" "~" (at 0 0 0) (effects (font (size 1.27 1.27)) (hide yes)))\n'
        '    (symbol "D_Schottky_0_1"\n'
        '      (rectangle (start -0.762 -1.016) (end 0.762 1.016))\n'
        '    )\n'
        '    (symbol "D_Schottky_1_1"\n'
        '      (pin passive line (at -2.54 0 0) (length 2.54)\n'
        '        (name "K" (effects (font (size 1.27 1.27))))\n'
        '        (number "1" (effects (font (size 1.27 1.27)))))\n'
        '      (pin passive line (at 2.54 0 180) (length 2.54)\n'
        '        (name "A" (effects (font (size 1.27 1.27))))\n'
        '        (number "2" (effects (font (size 1.27 1.27)))))\n'
        '    )\n'
        '  )'
    )

    # -------------------------------------------------------------------------
    # Symbol 8: Regulator_Linear:LM7805_TO220
    # -------------------------------------------------------------------------
    parts.append(
        '  (symbol "Regulator_Linear:LM7805_TO220" (pin_numbers (hide yes)) (pin_names (offset 1.016))\n'
        '    (property "Reference" "U" (at 0 7.62 0) (effects (font (size 1.27 1.27))))\n'
        '    (property "Value" "LM7805_TO220" (at 0 10.16 0) (effects (font (size 1.27 1.27))))\n'
        '    (property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) (hide yes)))\n'
        '    (property "Datasheet" "~" (at 0 0 0) (effects (font (size 1.27 1.27)) (hide yes)))\n'
        '    (symbol "LM7805_TO220_0_1"\n'
        '      (rectangle (start -5.08 -5.08) (end 5.08 5.08))\n'
        '    )\n'
        '    (symbol "LM7805_TO220_1_1"\n'
        '      (pin input line (at -7.62 0 0) (length 2.54)\n'
        '        (name "VI" (effects (font (size 1.27 1.27))))\n'
        '        (number "1" (effects (font (size 1.27 1.27)))))\n'
        '      (pin power_in line (at 0 -7.62 90) (length 2.54)\n'
        '        (name "GND" (effects (font (size 1.27 1.27))))\n'
        '        (number "2" (effects (font (size 1.27 1.27)))))\n'
        '      (pin output line (at 7.62 0 180) (length 2.54)\n'
        '        (name "VO" (effects (font (size 1.27 1.27))))\n'
        '        (number "3" (effects (font (size 1.27 1.27)))))\n'
        '    )\n'
        '  )'
    )

    # -------------------------------------------------------------------------
    # Symbol 9: Amplifier_Operational:TL072  (3 units: A, B, power)
    # -------------------------------------------------------------------------
    tl072_body = (
        '      (polyline (pts (xy -5.08 5.08) (xy 5.08 0) (xy -5.08 -5.08) (xy -5.08 5.08))'
        ' (stroke (width 0) (type default)) (fill (type none)))\n'
    )
    parts.append(
        '  (symbol "Amplifier_Operational:TL072" (pin_numbers (hide yes)) (pin_names (offset 1.016))\n'
        '    (property "Reference" "U" (at 0 7.62 0) (effects (font (size 1.27 1.27))))\n'
        '    (property "Value" "TL072" (at 0 10.16 0) (effects (font (size 1.27 1.27))))\n'
        '    (property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) (hide yes)))\n'
        '    (property "Datasheet" "~" (at 0 0 0) (effects (font (size 1.27 1.27)) (hide yes)))\n'
        '    (symbol "TL072_0_1"\n'
        + tl072_body +
        '    )\n'
        '    (symbol "TL072_1_1"\n'
        '      (pin output line (at 7.62 0 180) (length 2.54)\n'
        '        (name "OUT" (effects (font (size 1.27 1.27))))\n'
        '        (number "1" (effects (font (size 1.27 1.27)))))\n'
        '      (pin input line (at -7.62 2.54 0) (length 2.54)\n'
        '        (name "IN-" (effects (font (size 1.27 1.27))))\n'
        '        (number "2" (effects (font (size 1.27 1.27)))))\n'
        '      (pin input line (at -7.62 -2.54 0) (length 2.54)\n'
        '        (name "IN+" (effects (font (size 1.27 1.27))))\n'
        '        (number "3" (effects (font (size 1.27 1.27)))))\n'
        '    )\n'
        '    (symbol "TL072_0_2"\n'
        + tl072_body +
        '    )\n'
        '    (symbol "TL072_2_1"\n'
        '      (pin output line (at 7.62 0 180) (length 2.54)\n'
        '        (name "OUT" (effects (font (size 1.27 1.27))))\n'
        '        (number "5" (effects (font (size 1.27 1.27)))))\n'
        '      (pin input line (at -7.62 2.54 0) (length 2.54)\n'
        '        (name "IN-" (effects (font (size 1.27 1.27))))\n'
        '        (number "6" (effects (font (size 1.27 1.27)))))\n'
        '      (pin input line (at -7.62 -2.54 0) (length 2.54)\n'
        '        (name "IN+" (effects (font (size 1.27 1.27))))\n'
        '        (number "7" (effects (font (size 1.27 1.27)))))\n'
        '    )\n'
        '    (symbol "TL072_3_1"\n'
        '      (pin power_in line (at 0 2.54 270) (length 2.54)\n'
        '        (name "V+" (effects (font (size 1.27 1.27))))\n'
        '        (number "8" (effects (font (size 1.27 1.27)))))\n'
        '      (pin power_in line (at 0 -2.54 90) (length 2.54)\n'
        '        (name "V-" (effects (font (size 1.27 1.27))))\n'
        '        (number "4" (effects (font (size 1.27 1.27)))))\n'
        '    )\n'
        '  )'
    )

    # -------------------------------------------------------------------------
    # Symbol 10: Isolator:6N137
    # -------------------------------------------------------------------------
    parts.append(
        '  (symbol "Isolator:6N137" (pin_numbers (hide yes)) (pin_names (offset 1.016))\n'
        '    (property "Reference" "U" (at 0 10.16 0) (effects (font (size 1.27 1.27))))\n'
        '    (property "Value" "6N137" (at 0 12.7 0) (effects (font (size 1.27 1.27))))\n'
        '    (property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) (hide yes)))\n'
        '    (property "Datasheet" "~" (at 0 0 0) (effects (font (size 1.27 1.27)) (hide yes)))\n'
        '    (symbol "6N137_0_1"\n'
        '      (rectangle (start -7.62 -7.62) (end 7.62 7.62))\n'
        '    )\n'
        '    (symbol "6N137_1_1"\n'
        '      (pin no_connect line (at -10.16 7.62 0) (length 2.54)\n'
        '        (name "NC" (effects (font (size 1.27 1.27))))\n'
        '        (number "1" (effects (font (size 1.27 1.27)))))\n'
        '      (pin input line (at -10.16 5.08 0) (length 2.54)\n'
        '        (name "A" (effects (font (size 1.27 1.27))))\n'
        '        (number "2" (effects (font (size 1.27 1.27)))))\n'
        '      (pin input line (at -10.16 2.54 0) (length 2.54)\n'
        '        (name "C" (effects (font (size 1.27 1.27))))\n'
        '        (number "3" (effects (font (size 1.27 1.27)))))\n'
        '      (pin no_connect line (at -10.16 0 0) (length 2.54)\n'
        '        (name "NC" (effects (font (size 1.27 1.27))))\n'
        '        (number "4" (effects (font (size 1.27 1.27)))))\n'
        '      (pin power_in line (at -10.16 -2.54 0) (length 2.54)\n'
        '        (name "GND" (effects (font (size 1.27 1.27))))\n'
        '        (number "5" (effects (font (size 1.27 1.27)))))\n'
        '      (pin output line (at 10.16 -2.54 180) (length 2.54)\n'
        '        (name "Vo" (effects (font (size 1.27 1.27))))\n'
        '        (number "6" (effects (font (size 1.27 1.27)))))\n'
        '      (pin input line (at 10.16 0 180) (length 2.54)\n'
        '        (name "VE" (effects (font (size 1.27 1.27))))\n'
        '        (number "7" (effects (font (size 1.27 1.27)))))\n'
        '      (pin power_in line (at 10.16 2.54 180) (length 2.54)\n'
        '        (name "VCC" (effects (font (size 1.27 1.27))))\n'
        '        (number "8" (effects (font (size 1.27 1.27)))))\n'
        '    )\n'
        '  )'
    )

    # -------------------------------------------------------------------------
    # Symbol 11: Connector:Conn_02x08_Odd_Even  (16-pin Eurorack power)
    # -------------------------------------------------------------------------
    conn_left = [
        (1,  "P1",  17.78),
        (3,  "P3",  15.24),
        (5,  "P5",  12.70),
        (7,  "P7",  10.16),
        (9,  "P9",   7.62),
        (11, "P11",  5.08),
        (13, "P13",  2.54),
        (15, "P15",  0.00),
    ]
    conn_right = [
        (2,  "P2",  17.78),
        (4,  "P4",  15.24),
        (6,  "P6",  12.70),
        (8,  "P8",  10.16),
        (10, "P10",  7.62),
        (12, "P12",  5.08),
        (14, "P14",  2.54),
        (16, "P16",  0.00),
    ]

    conn_pin_lines = []
    for (n, name, y) in conn_left:
        conn_pin_lines.append(
            f'    (pin passive line (at -7.62 {y} 0) (length 2.54)\n'
            f'      (name "{name}" (effects (font (size 1.27 1.27))))\n'
            f'      (number "{n}" (effects (font (size 1.27 1.27)))))'
        )
    for (n, name, y) in conn_right:
        conn_pin_lines.append(
            f'    (pin passive line (at 7.62 {y} 180) (length 2.54)\n'
            f'      (name "{name}" (effects (font (size 1.27 1.27))))\n'
            f'      (number "{n}" (effects (font (size 1.27 1.27)))))'
        )

    parts.append(
        '  (symbol "Connector:Conn_02x08_Odd_Even" (pin_numbers (hide yes)) (pin_names (offset 1.016))\n'
        '    (property "Reference" "J" (at 0 22.86 0) (effects (font (size 1.27 1.27))))\n'
        '    (property "Value" "Conn_02x08_Odd_Even" (at 0 25.4 0) (effects (font (size 1.27 1.27))))\n'
        '    (property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) (hide yes)))\n'
        '    (property "Datasheet" "~" (at 0 0 0) (effects (font (size 1.27 1.27)) (hide yes)))\n'
        '    (symbol "Conn_02x08_Odd_Even_0_1"\n'
        '      (rectangle (start -5.08 -2.54) (end 5.08 20.32))\n'
        '    )\n'
        '    (symbol "Conn_02x08_Odd_Even_1_1"\n'
        + "\n".join(conn_pin_lines) + "\n"
        '    )\n'
        '  )'
    )

    # -------------------------------------------------------------------------
    # Symbol 12: Connector_Audio:AudioJack2
    # -------------------------------------------------------------------------
    parts.append(
        '  (symbol "Connector_Audio:AudioJack2" (pin_numbers (hide yes)) (pin_names (offset 1.016))\n'
        '    (property "Reference" "J" (at 0 5.08 0) (effects (font (size 1.27 1.27))))\n'
        '    (property "Value" "AudioJack2" (at 0 7.62 0) (effects (font (size 1.27 1.27))))\n'
        '    (property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) (hide yes)))\n'
        '    (property "Datasheet" "~" (at 0 0 0) (effects (font (size 1.27 1.27)) (hide yes)))\n'
        '    (symbol "AudioJack2_0_1"\n'
        '      (rectangle (start -5.08 -2.54) (end 5.08 2.54))\n'
        '    )\n'
        '    (symbol "AudioJack2_1_1"\n'
        '      (pin passive line (at -7.62 0 0) (length 2.54)\n'
        '        (name "T" (effects (font (size 1.27 1.27))))\n'
        '        (number "1" (effects (font (size 1.27 1.27)))))\n'
        '      (pin passive line (at 7.62 0 180) (length 2.54)\n'
        '        (name "S" (effects (font (size 1.27 1.27))))\n'
        '        (number "2" (effects (font (size 1.27 1.27)))))\n'
        '    )\n'
        '  )'
    )

    # -------------------------------------------------------------------------
    # Symbol 13: Connector_DIN:DIN-5_270
    # -------------------------------------------------------------------------
    parts.append(
        '  (symbol "Connector_DIN:DIN-5_270" (pin_numbers (hide yes)) (pin_names (offset 1.016))\n'
        '    (property "Reference" "J" (at 0 7.62 0) (effects (font (size 1.27 1.27))))\n'
        '    (property "Value" "DIN-5_270" (at 0 10.16 0) (effects (font (size 1.27 1.27))))\n'
        '    (property "Footprint" "" (at 0 0 0) (effects (font (size 1.27 1.27)) (hide yes)))\n'
        '    (property "Datasheet" "~" (at 0 0 0) (effects (font (size 1.27 1.27)) (hide yes)))\n'
        '    (symbol "DIN-5_270_0_1"\n'
        '      (rectangle (start -5.08 -5.08) (end 5.08 5.08))\n'
        '    )\n'
        '    (symbol "DIN-5_270_1_1"\n'
        '      (pin passive line (at -7.62 5.08 0) (length 2.54)\n'
        '        (name "P1" (effects (font (size 1.27 1.27))))\n'
        '        (number "1" (effects (font (size 1.27 1.27)))))\n'
        '      (pin passive line (at -7.62 2.54 0) (length 2.54)\n'
        '        (name "P2" (effects (font (size 1.27 1.27))))\n'
        '        (number "2" (effects (font (size 1.27 1.27)))))\n'
        '      (pin passive line (at -7.62 0 0) (length 2.54)\n'
        '        (name "P3" (effects (font (size 1.27 1.27))))\n'
        '        (number "3" (effects (font (size 1.27 1.27)))))\n'
        '      (pin passive line (at -7.62 -2.54 0) (length 2.54)\n'
        '        (name "P4" (effects (font (size 1.27 1.27))))\n'
        '        (number "4" (effects (font (size 1.27 1.27)))))\n'
        '      (pin passive line (at -7.62 -5.08 0) (length 2.54)\n'
        '        (name "P5" (effects (font (size 1.27 1.27))))\n'
        '        (number "5" (effects (font (size 1.27 1.27)))))\n'
        '    )\n'
        '  )'
    )

    return "\n".join(parts)
