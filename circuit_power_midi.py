import uuid


def gen_uuid():
    return str(uuid.uuid4())


def get_power_midi_elements() -> str:
    elements = []

    # =========================================================================
    # POWER SECTION
    # =========================================================================

    # -------------------------------------------------------------------------
    # J1 -- Eurorack 16-pin IDC power connector
    # Connector:Conn_02x08_Odd_Even at (25, 45), rotation=0
    # -------------------------------------------------------------------------
    j1_uuid = gen_uuid()
    elements.append(
        f'(symbol (lib_id "Connector:Conn_02x08_Odd_Even") (at 25 45 0) (unit 1)\n'
        f'  (in_bom yes) (on_board yes) (dnp no) (uuid "{j1_uuid}")\n'
        f'  (property "Reference" "J1" (at 27 43 0) (effects (font (size 1.27 1.27))))\n'
        f'  (property "Value" "Eurorack_IDC16" (at 27 44.27 0) (effects (font (size 1.27 1.27))))\n'
        f'  (property "Footprint" "Connector_IDC:IDC-Header_2x08_P2.54mm_Vertical" (at 25 45 0) (effects (font (size 1.27 1.27)) (hide yes)))\n'
        f'  (property "Datasheet" "~" (at 25 45 0) (effects (font (size 1.27 1.27)) (hide yes)))\n'
        f'  (pin "1"  (uuid "{gen_uuid()}"))\n'
        f'  (pin "2"  (uuid "{gen_uuid()}"))\n'
        f'  (pin "3"  (uuid "{gen_uuid()}"))\n'
        f'  (pin "4"  (uuid "{gen_uuid()}"))\n'
        f'  (pin "5"  (uuid "{gen_uuid()}"))\n'
        f'  (pin "6"  (uuid "{gen_uuid()}"))\n'
        f'  (pin "7"  (uuid "{gen_uuid()}"))\n'
        f'  (pin "8"  (uuid "{gen_uuid()}"))\n'
        f'  (pin "9"  (uuid "{gen_uuid()}"))\n'
        f'  (pin "10" (uuid "{gen_uuid()}"))\n'
        f'  (pin "11" (uuid "{gen_uuid()}"))\n'
        f'  (pin "12" (uuid "{gen_uuid()}"))\n'
        f'  (pin "13" (uuid "{gen_uuid()}"))\n'
        f'  (pin "14" (uuid "{gen_uuid()}"))\n'
        f'  (pin "15" (uuid "{gen_uuid()}"))\n'
        f'  (pin "16" (uuid "{gen_uuid()}"))\n'
        f')'
    )

    # Geometric helpers
    lx       = 19.92   # left-side pin exit x
    rx       = 30.08   # right-side pin exit x
    label_lx = 12.7    # global label anchor x (left)
    label_rx = 38.1    # global label anchor x (right)
    wire_lx  = 15.24   # inner wire end x (left)
    wire_rx  = 34.54   # inner wire end x (right)
    row_y = [36.83 + i * 2.54 for i in range(8)]

    def _wire(x1, y1, x2, y2):
        return (
            f'(wire (pts (xy {x1} {y1:.2f}) (xy {x2} {y2:.2f}))'
            f' (stroke (width 0) (type default)) (uuid "{gen_uuid()}"))'
        )

    def _glabel(name, x, y, angle):
        justify = "right" if angle == 180 else "left"
        return (
            f'(global_label "{name}" (shape input) (at {x} {y:.4f} {angle})'
            f' (fields_autoplaced yes)\n'
            f'  (effects (font (size 1.27 1.27)) (justify {justify})) (uuid "{gen_uuid()}")\n'
            f'  (property "Intersheet References" "" (at 0 0 0)'
            f' (effects (font (size 1.27 1.27)) (hide yes))))'
        )

    def _label(name, x, y):
        return (
            f'(label "{name}" (at {x} {y:.4f} 0) (fields_autoplaced yes)\n'
            f'  (effects (font (size 1.27 1.27)) (justify left bottom)) (uuid "{gen_uuid()}"))'
        )

    def _noconn(x, y):
        return f'(no_connect (at {x} {y:.2f}) (uuid "{gen_uuid()}"))'

    # --- J1 odd pins (left side) ---
    elements.append(_wire(lx, row_y[0], wire_lx, row_y[0]))
    elements.append(_glabel("+12V", label_lx, row_y[0], 180))
    elements.append(_wire(lx, row_y[1], wire_lx, row_y[1]))
    elements.append(_glabel("+12V", label_lx, row_y[1], 180))
    elements.append(_noconn(lx, row_y[2]))
    elements.append(_wire(lx, row_y[3], wire_lx, row_y[3]))
    elements.append(_glabel("GND", label_lx, row_y[3], 180))
    elements.append(_wire(lx, row_y[4], wire_lx, row_y[4]))
    elements.append(_glabel("GND", label_lx, row_y[4], 180))
    elements.append(_wire(lx, row_y[5], wire_lx, row_y[5]))
    elements.append(_glabel("GND", label_lx, row_y[5], 180))
    elements.append(_wire(lx, row_y[6], wire_lx, row_y[6]))
    elements.append(_glabel("-12V", label_lx, row_y[6], 180))
    elements.append(_wire(lx, row_y[7], wire_lx, row_y[7]))
    elements.append(_glabel("-12V", label_lx, row_y[7], 180))

    # --- J1 even pins (right side) ---
    elements.append(_wire(rx, row_y[0], wire_rx, row_y[0]))
    elements.append(_glabel("+12V", label_rx, row_y[0], 0))
    elements.append(_wire(rx, row_y[1], wire_rx, row_y[1]))
    elements.append(_glabel("+12V", label_rx, row_y[1], 0))
    elements.append(_noconn(rx, row_y[2]))
    elements.append(_wire(rx, row_y[3], wire_rx, row_y[3]))
    elements.append(_glabel("GND", label_rx, row_y[3], 0))
    elements.append(_wire(rx, row_y[4], wire_rx, row_y[4]))
    elements.append(_glabel("GND", label_rx, row_y[4], 0))
    elements.append(_wire(rx, row_y[5], wire_rx, row_y[5]))
    elements.append(_glabel("GND", label_rx, row_y[5], 0))
    elements.append(_wire(rx, row_y[6], wire_rx, row_y[6]))
    elements.append(_glabel("-12V", label_rx, row_y[6], 0))
    elements.append(_wire(rx, row_y[7], wire_rx, row_y[7]))
    elements.append(_glabel("-12V", label_rx, row_y[7], 0))

    # -------------------------------------------------------------------------
    # D1 -- 1N4001 reverse polarity protection
    # Device:D at (55, 25), rotation=0
    # Pin 2 (anode) at (52.46, 25), Pin 1 (cathode) at (57.54, 25)
    # -------------------------------------------------------------------------
    d1_uuid = gen_uuid()
    elements.append(
        f'(symbol (lib_id "Device:D") (at 55 25 0) (unit 1)\n'
        f'  (in_bom yes) (on_board yes) (dnp no) (uuid "{d1_uuid}")\n'
        f'  (property "Reference" "D1" (at 55 22.5 0) (effects (font (size 1.27 1.27))))\n'
        f'  (property "Value" "1N4001" (at 55 23.77 0) (effects (font (size 1.27 1.27))))\n'
        f'  (property "Footprint" "Diode_THT:D_DO-41_SOD81_P10.16mm_Horizontal"'
        f' (at 55 25 0) (effects (font (size 1.27 1.27)) (hide yes)))\n'
        f'  (property "Datasheet" "~" (at 55 25 0) (effects (font (size 1.27 1.27)) (hide yes)))\n'
        f'  (pin "1" (uuid "{gen_uuid()}"))\n'
        f'  (pin "2" (uuid "{gen_uuid()}"))\n'
        f')'
    )
    elements.append(_wire(52.46, 25, 49.16, 25))
    elements.append(_glabel("+12V", 49.16, 25, 180))
    elements.append(_wire(57.54, 25, 65, 25))
    elements.append(_label("+12V_RECT", 65, 25))

    # -------------------------------------------------------------------------
    # U5 -- LM7805 voltage regulator at (85, 25)
    # Pin 1 (VI) at (77.38, 25), Pin 2 (GND) at (85, 32.62), Pin 3 (VO) at (92.62, 25)
    # -------------------------------------------------------------------------
    u5_uuid = gen_uuid()
    elements.append(
        f'(symbol (lib_id "Regulator_Linear:LM7805_TO220") (at 85 25 0) (unit 1)\n'
        f'  (in_bom yes) (on_board yes) (dnp no) (uuid "{u5_uuid}")\n'
        f'  (property "Reference" "U5" (at 85 22 0) (effects (font (size 1.27 1.27))))\n'
        f'  (property "Value" "LM7805" (at 85 23.27 0) (effects (font (size 1.27 1.27))))\n'
        f'  (property "Footprint" "Package_TO_SOT_THT:TO-220-3_Vertical"'
        f' (at 85 25 0) (effects (font (size 1.27 1.27)) (hide yes)))\n'
        f'  (property "Datasheet" "~" (at 85 25 0) (effects (font (size 1.27 1.27)) (hide yes)))\n'
        f'  (pin "1" (uuid "{gen_uuid()}"))\n'
        f'  (pin "2" (uuid "{gen_uuid()}"))\n'
        f'  (pin "3" (uuid "{gen_uuid()}"))\n'
        f')'
    )
    elements.append(_wire(77.38, 25, 70, 25))
    elements.append(_label("+12V_RECT", 70, 25))
    elements.append(_wire(85, 32.62, 85, 37.62))
    elements.append(_glabel("GND", 85, 37.62, 270))
    elements.append(_wire(92.62, 25, 100, 25))
    elements.append(_glabel("+5V", 100, 25, 0))

    # -------------------------------------------------------------------------
    # C5 -- 10uF electrolytic (LM7805 input bypass) at (75, 40)
    # -------------------------------------------------------------------------
    c5_uuid = gen_uuid()
    elements.append(
        f'(symbol (lib_id "Device:C_Polarized") (at 75 40 0) (unit 1)\n'
        f'  (in_bom yes) (on_board yes) (dnp no) (uuid "{c5_uuid}")\n'
        f'  (property "Reference" "C5" (at 77.27 39 0) (effects (font (size 1.27 1.27))))\n'
        f'  (property "Value" "10uF" (at 77.27 40.27 0) (effects (font (size 1.27 1.27))))\n'
        f'  (property "Footprint" "Capacitor_THT:CP_Radial_D5.0mm_P2.50mm"'
        f' (at 75 40 0) (effects (font (size 1.27 1.27)) (hide yes)))\n'
        f'  (property "Datasheet" "~" (at 75 40 0) (effects (font (size 1.27 1.27)) (hide yes)))\n'
        f'  (pin "1" (uuid "{gen_uuid()}"))\n'
        f'  (pin "2" (uuid "{gen_uuid()}"))\n'
        f')'
    )
    elements.append(_wire(75, 37.46, 75, 32))
    elements.append(_label("+12V_RECT", 75, 32))
    elements.append(_wire(75, 42.54, 75, 47.54))
    elements.append(_glabel("GND", 75, 47.54, 270))

    # -------------------------------------------------------------------------
    # C6 -- 10uF electrolytic (LM7805 output bypass) at (100, 40)
    # -------------------------------------------------------------------------
    c6_uuid = gen_uuid()
    elements.append(
        f'(symbol (lib_id "Device:C_Polarized") (at 100 40 0) (unit 1)\n'
        f'  (in_bom yes) (on_board yes) (dnp no) (uuid "{c6_uuid}")\n'
        f'  (property "Reference" "C6" (at 102.27 39 0) (effects (font (size 1.27 1.27))))\n'
        f'  (property "Value" "10uF" (at 102.27 40.27 0) (effects (font (size 1.27 1.27))))\n'
        f'  (property "Footprint" "Capacitor_THT:CP_Radial_D5.0mm_P2.50mm"'
        f' (at 100 40 0) (effects (font (size 1.27 1.27)) (hide yes)))\n'
        f'  (property "Datasheet" "~" (at 100 40 0) (effects (font (size 1.27 1.27)) (hide yes)))\n'
        f'  (pin "1" (uuid "{gen_uuid()}"))\n'
        f'  (pin "2" (uuid "{gen_uuid()}"))\n'
        f')'
    )
    elements.append(_wire(100, 37.46, 100, 32))
    elements.append(_glabel("+5V", 100, 32, 90))
    elements.append(_wire(100, 42.54, 100, 47.54))
    elements.append(_glabel("GND", 100, 47.54, 270))

    # -------------------------------------------------------------------------
    # C7 -- 100nF bypass (AY-3-8910 VCC) at (120, 40)
    # -------------------------------------------------------------------------
    c7_uuid = gen_uuid()
    elements.append(
        f'(symbol (lib_id "Device:C") (at 120 40 0) (unit 1)\n'
        f'  (in_bom yes) (on_board yes) (dnp no) (uuid "{c7_uuid}")\n'
        f'  (property "Reference" "C7" (at 122.27 39 0) (effects (font (size 1.27 1.27))))\n'
        f'  (property "Value" "100nF" (at 122.27 40.27 0) (effects (font (size 1.27 1.27))))\n'
        f'  (property "Footprint" "Capacitor_THT:C_Disc_D4.7mm_W2.5mm_P5.00mm"'
        f' (at 120 40 0) (effects (font (size 1.27 1.27)) (hide yes)))\n'
        f'  (property "Datasheet" "~" (at 120 40 0) (effects (font (size 1.27 1.27)) (hide yes)))\n'
        f'  (pin "1" (uuid "{gen_uuid()}"))\n'
        f'  (pin "2" (uuid "{gen_uuid()}"))\n'
        f')'
    )
    elements.append(_wire(120, 37.46, 120, 32))
    elements.append(_glabel("+5V", 120, 32, 90))
    elements.append(_wire(120, 42.54, 120, 47.54))
    elements.append(_glabel("GND", 120, 47.54, 270))

    # -------------------------------------------------------------------------
    # C8 -- 100nF bypass (Arduino VCC) at (135, 40)
    # -------------------------------------------------------------------------
    c8_uuid = gen_uuid()
    elements.append(
        f'(symbol (lib_id "Device:C") (at 135 40 0) (unit 1)\n'
        f'  (in_bom yes) (on_board yes) (dnp no) (uuid "{c8_uuid}")\n'
        f'  (property "Reference" "C8" (at 137.27 39 0) (effects (font (size 1.27 1.27))))\n'
        f'  (property "Value" "100nF" (at 137.27 40.27 0) (effects (font (size 1.27 1.27))))\n'
        f'  (property "Footprint" "Capacitor_THT:C_Disc_D4.7mm_W2.5mm_P5.00mm"'
        f' (at 135 40 0) (effects (font (size 1.27 1.27)) (hide yes)))\n'
        f'  (property "Datasheet" "~" (at 135 40 0) (effects (font (size 1.27 1.27)) (hide yes)))\n'
        f'  (pin "1" (uuid "{gen_uuid()}"))\n'
        f'  (pin "2" (uuid "{gen_uuid()}"))\n'
        f')'
    )
    elements.append(_wire(135, 37.46, 135, 32))
    elements.append(_glabel("+5V", 135, 32, 90))
    elements.append(_wire(135, 42.54, 135, 47.54))
    elements.append(_glabel("GND", 135, 47.54, 270))

    # =========================================================================
    # MIDI INPUT SECTION
    # =========================================================================

    # -------------------------------------------------------------------------
    # J2 -- MIDI DIN-5 at (285, 45)
    # -------------------------------------------------------------------------
    j2_uuid = gen_uuid()
    elements.append(
        f'(symbol (lib_id "Connector_DIN:DIN-5_270") (at 285 45 0) (unit 1)\n'
        f'  (in_bom yes) (on_board yes) (dnp no) (uuid "{j2_uuid}")\n'
        f'  (property "Reference" "J2" (at 287 43 0) (effects (font (size 1.27 1.27))))\n'
        f'  (property "Value" "MIDI_IN" (at 287 44.27 0) (effects (font (size 1.27 1.27))))\n'
        f'  (property "Footprint" "Connector_DIN:DIN5_262Degree_THT"'
        f' (at 285 45 0) (effects (font (size 1.27 1.27)) (hide yes)))\n'
        f'  (property "Datasheet" "~" (at 285 45 0) (effects (font (size 1.27 1.27)) (hide yes)))\n'
        f'  (pin "1" (uuid "{gen_uuid()}"))\n'
        f'  (pin "2" (uuid "{gen_uuid()}"))\n'
        f'  (pin "3" (uuid "{gen_uuid()}"))\n'
        f'  (pin "4" (uuid "{gen_uuid()}"))\n'
        f'  (pin "5" (uuid "{gen_uuid()}"))\n'
        f')'
    )
    # Pin 1 no_connect, Pin 3 no_connect
    elements.append(_noconn(277.38, 50.08))   # pin 1 exits left
    elements.append(_noconn(277.38, 45.00))   # pin 3 exits left
    # Pin 2 (shield) -> GND
    elements.append(_wire(277.38, 47.54, 272, 47.54))
    elements.append(_glabel("GND", 272, 47.54, 180))
    # Pin 4 (+current) exits right -> wire to R1 pin 1
    elements.append(_wire(292.62, 42.46, 308, 42.46))
    elements.append(_wire(308, 42.46, 308, 38))
    elements.append(_wire(308, 38, 311.27, 38))
    # Pin 5 (return) exits right -> wire to D2 anode
    elements.append(_wire(292.62, 47.54, 308, 47.54))
    elements.append(_wire(308, 47.54, 308, 55))
    elements.append(_wire(308, 55, 311.27, 55))

    # -------------------------------------------------------------------------
    # R1 -- 220R MIDI current limit at (315, 38), rotation=0
    # Pin 1 at (311.27, 38), Pin 2 at (318.73, 38)
    # -------------------------------------------------------------------------
    r1_uuid = gen_uuid()
    elements.append(
        f'(symbol (lib_id "Device:R") (at 315 38 0) (unit 1)\n'
        f'  (in_bom yes) (on_board yes) (dnp no) (uuid "{r1_uuid}")\n'
        f'  (property "Reference" "R1" (at 315 36 0) (effects (font (size 1.27 1.27))))\n'
        f'  (property "Value" "220R" (at 315 37.27 0) (effects (font (size 1.27 1.27))))\n'
        f'  (property "Footprint"'
        f' "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal"'
        f' (at 315 38 0) (effects (font (size 1.27 1.27)) (hide yes)))\n'
        f'  (property "Datasheet" "~" (at 315 38 0) (effects (font (size 1.27 1.27)) (hide yes)))\n'
        f'  (pin "1" (uuid "{gen_uuid()}"))\n'
        f'  (pin "2" (uuid "{gen_uuid()}"))\n'
        f')'
    )
    # R1 pin 2 -> U3 pin 2 (anode)
    elements.append(_wire(318.73, 38, 335, 38))
    elements.append(_wire(335, 38, 335, 44.92))
    elements.append(_wire(335, 44.92, 339.38, 44.92))

    # -------------------------------------------------------------------------
    # D2 -- 1N4148 MIDI protection at (315, 55), rotation=0
    # Pin 2 (anode) at (311.27, 55), Pin 1 (cathode) at (318.73, 55)
    # -------------------------------------------------------------------------
    d2_uuid = gen_uuid()
    elements.append(
        f'(symbol (lib_id "Device:D") (at 315 55 0) (unit 1)\n'
        f'  (in_bom yes) (on_board yes) (dnp no) (uuid "{d2_uuid}")\n'
        f'  (property "Reference" "D2" (at 315 52.5 0) (effects (font (size 1.27 1.27))))\n'
        f'  (property "Value" "1N4148" (at 315 53.77 0) (effects (font (size 1.27 1.27))))\n'
        f'  (property "Footprint" "Diode_THT:D_DO-35_SOD27_P7.62mm_Horizontal"'
        f' (at 315 55 0) (effects (font (size 1.27 1.27)) (hide yes)))\n'
        f'  (property "Datasheet" "~" (at 315 55 0) (effects (font (size 1.27 1.27)) (hide yes)))\n'
        f'  (pin "1" (uuid "{gen_uuid()}"))\n'
        f'  (pin "2" (uuid "{gen_uuid()}"))\n'
        f')'
    )
    # D2 cathode -> U3 pin 3 (cathode side)
    elements.append(_wire(318.73, 55, 335, 55))
    elements.append(_wire(335, 55, 335, 47.46))
    elements.append(_wire(335, 47.46, 339.38, 47.46))

    # -------------------------------------------------------------------------
    # U3 -- 6N137 optocoupler at (350, 50)
    # Left pins exit at x=339.38; Right pins exit at x=360.62
    # y positions (4 rows): 44.92, 47.46, 50.00, 52.54
    # -------------------------------------------------------------------------
    u3_uuid = gen_uuid()
    elements.append(
        f'(symbol (lib_id "Isolator:6N137") (at 350 50 0) (unit 1)\n'
        f'  (in_bom yes) (on_board yes) (dnp no) (uuid "{u3_uuid}")\n'
        f'  (property "Reference" "U3" (at 350 40.5 0) (effects (font (size 1.27 1.27))))\n'
        f'  (property "Value" "6N137" (at 350 41.77 0) (effects (font (size 1.27 1.27))))\n'
        f'  (property "Footprint" "Package_DIP:DIP-8_W7.62mm"'
        f' (at 350 50 0) (effects (font (size 1.27 1.27)) (hide yes)))\n'
        f'  (property "Datasheet" "~" (at 350 50 0) (effects (font (size 1.27 1.27)) (hide yes)))\n'
        f'  (pin "1" (uuid "{gen_uuid()}"))\n'
        f'  (pin "2" (uuid "{gen_uuid()}"))\n'
        f'  (pin "3" (uuid "{gen_uuid()}"))\n'
        f'  (pin "4" (uuid "{gen_uuid()}"))\n'
        f'  (pin "5" (uuid "{gen_uuid()}"))\n'
        f'  (pin "6" (uuid "{gen_uuid()}"))\n'
        f'  (pin "7" (uuid "{gen_uuid()}"))\n'
        f'  (pin "8" (uuid "{gen_uuid()}"))\n'
        f')'
    )
    # Pin 1 (NC) and Pin 4 (NC): no_connect
    elements.append(_noconn(339.38, 44.92))
    elements.append(_noconn(339.38, 52.54))
    # Pin 5 (GND) -> GND
    elements.append(_wire(360.62, 52.54, 368, 52.54))
    elements.append(_glabel("GND", 368, 52.54, 0))
    # Pin 6 (Vo) -> R2 junction + MIDI_RX label
    elements.append(_wire(360.62, 50.00, 375, 50.00))
    elements.append(_wire(375, 50.00, 375, 46.78))
    elements.append(_label("MIDI_RX", 360.62, 50.00))
    # Pin 7 (VE enable) -> +5V
    elements.append(_wire(360.62, 47.46, 368, 47.46))
    elements.append(_glabel("+5V", 368, 47.46, 0))
    # Pin 8 (VCC) -> +5V
    elements.append(_wire(360.62, 44.92, 368, 44.92))
    elements.append(_glabel("+5V", 368, 44.92, 0))

    # -------------------------------------------------------------------------
    # R2 -- 10k pull-up for 6N137 Vo output at (375, 45), rotation=90
    # Pin 1 (top) at (375, 41.27), Pin 2 (bottom) at (375, 46.78) -- approx
    # -------------------------------------------------------------------------
    r2_uuid = gen_uuid()
    elements.append(
        f'(symbol (lib_id "Device:R") (at 375 45 90) (unit 1)\n'
        f'  (in_bom yes) (on_board yes) (dnp no) (uuid "{r2_uuid}")\n'
        f'  (property "Reference" "R2" (at 377.27 45 0) (effects (font (size 1.27 1.27))))\n'
        f'  (property "Value" "10k" (at 377.27 46.27 0) (effects (font (size 1.27 1.27))))\n'
        f'  (property "Footprint"'
        f' "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal"'
        f' (at 375 45 0) (effects (font (size 1.27 1.27)) (hide yes)))\n'
        f'  (property "Datasheet" "~" (at 375 45 0) (effects (font (size 1.27 1.27)) (hide yes)))\n'
        f'  (pin "1" (uuid "{gen_uuid()}"))\n'
        f'  (pin "2" (uuid "{gen_uuid()}"))\n'
        f')'
    )
    # R2 pin 1 (top) -> +5V
    elements.append(_wire(375, 41.27, 375, 37))
    elements.append(_glabel("+5V", 375, 37, 90))

    return "\n".join(elements)


if __name__ == "__main__":
    print(get_power_midi_elements())
