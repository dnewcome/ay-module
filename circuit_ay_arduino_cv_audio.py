import uuid


def gen_uuid():
    return str(uuid.uuid4())


def get_main_circuit_elements() -> str:
    elements = []

    # =========================================================================
    # AY-3-8910 SECTION
    # =========================================================================

    u1 = (
        f'(symbol (lib_id "Custom:AY-3-8910") (at 140 165 0) (unit 1)\n'
        f'  (in_bom yes) (on_board yes) (dnp no) (uuid "{gen_uuid()}")\n'
        f'  (property "Reference" "U1" (at 142 163 0) (effects (font (size 1.27 1.27))))\n'
        f'  (property "Value" "AY-3-8910" (at 142 165 0) (effects (font (size 1.27 1.27))))\n'
        f'  (property "Footprint" "Package_DIP:DIP-40_W15.24mm" (at 140 165 0)'
        f' (effects (font (size 1.27 1.27)) (hide yes)))\n'
        f'  (property "Datasheet" "~" (at 140 165 0)'
        f' (effects (font (size 1.27 1.27)) (hide yes)))\n'
    )
    for n in range(1, 41):
        u1 += f'  (pin "{n}" (uuid "{gen_uuid()}"))\n'
    u1 += ")"
    elements.append(u1)

    def lpy(n):
        return round(140.87 + (n - 1) * 2.54, 2)

    def rpy(n):
        return round(140.87 + (40 - n) * 2.54, 2)

    def wire(x1, y1, x2, y2):
        return (
            f'(wire (pts (xy {x1} {y1}) (xy {x2} {y2}))'
            f' (stroke (width 0) (type default)) (uuid "{gen_uuid()}"))'
        )

    def junction(x, y):
        return f'(junction (at {x} {y}) (diameter 0) (color 0 0 0 0) (uuid "{gen_uuid()}"))'

    def no_connect(x, y):
        return f'(no_connect (at {x} {y}) (uuid "{gen_uuid()}"))'

    def net_label(name, x, y, angle=0):
        justify = "right" if angle == 180 else "left"
        return (
            f'(label "{name}" (at {x} {y} {angle}) (fields_autoplaced yes)\n'
            f'  (effects (font (size 1.27 1.27)) (justify {justify} bottom))'
            f' (uuid "{gen_uuid()}"))'
        )

    def global_label(name, x, y, angle=0):
        justify = "right" if angle in (180, 270, 90) else "left"
        return (
            f'(global_label "{name}" (shape input) (at {x} {y} {angle})'
            f' (fields_autoplaced yes)\n'
            f'  (effects (font (size 1.27 1.27)) (justify {justify}))\n'
            f'  (uuid "{gen_uuid()}")\n'
            f'  (property "Intersheet References" "" (at 0 0 0)'
            f' (effects (font (size 1.27 1.27)) (hide yes))))'
        )

    # --- U1 Left side connections ---
    elements.append(wire(127.3, lpy(1), 122.3, lpy(1)))
    elements.append(global_label("GND", 122.3, lpy(1), 180))
    elements.append(no_connect(127.3, lpy(2)))
    elements.append(wire(127.3, lpy(3), 122.3, lpy(3)))
    elements.append(net_label("AY_AOUT_B", 122.3, lpy(3), 180))
    elements.append(wire(127.3, lpy(4), 122.3, lpy(4)))
    elements.append(net_label("AY_AOUT_A", 122.3, lpy(4), 180))
    elements.append(no_connect(127.3, lpy(5)))
    for n in range(6, 21):
        elements.append(no_connect(127.3, lpy(n)))

    # --- U1 Right side connections ---
    elements.append(no_connect(152.7, rpy(21)))

    py22 = rpy(22)
    elements.append(wire(152.7, py22, 157.7, py22))
    elements.append(net_label("AY_CLK", 157.7, py22, 0))

    py23 = rpy(23)
    elements.append(wire(152.7, py23, 157.7, py23))
    elements.append(net_label("AY_RST", 157.7, py23, 0))

    py24 = rpy(24)
    elements.append(wire(152.7, py24, 157.7, py24))
    elements.append(global_label("+5V", 157.7, py24, 0))

    py25 = rpy(25)
    elements.append(wire(152.7, py25, 157.7, py25))
    elements.append(global_label("GND", 157.7, py25, 0))

    elements.append(no_connect(152.7, rpy(26)))

    py27 = rpy(27)
    elements.append(wire(152.7, py27, 157.7, py27))
    elements.append(net_label("AY_BDIR", 157.7, py27, 0))

    py28 = rpy(28)
    elements.append(wire(152.7, py28, 157.7, py28))
    elements.append(net_label("AY_BC2", 157.7, py28, 0))

    py29 = rpy(29)
    elements.append(wire(152.7, py29, 157.7, py29))
    elements.append(global_label("GND", 157.7, py29, 0))

    da_map = {30:"DA7",31:"DA6",32:"DA5",33:"DA4",34:"DA3",35:"DA2",36:"DA1",37:"DA0"}
    for pin_n, lname in da_map.items():
        py = rpy(pin_n)
        elements.append(wire(152.7, py, 157.7, py))
        elements.append(net_label(lname, 157.7, py, 0))

    py38 = rpy(38)
    elements.append(wire(152.7, py38, 157.7, py38))
    elements.append(net_label("AY_AOUT_C", 157.7, py38, 0))

    elements.append(no_connect(152.7, rpy(39)))

    py40 = rpy(40)
    elements.append(wire(152.7, py40, 157.7, py40))
    elements.append(global_label("+5V", 157.7, py40, 0))

    # R3 — 10kΩ RESET pull-up at (165, py23)
    r3 = (
        f'(symbol (lib_id "Device:R") (at 165 {py23} 0) (unit 1)\n'
        f'  (in_bom yes) (on_board yes) (dnp no) (uuid "{gen_uuid()}")\n'
        f'  (property "Reference" "R3" (at 165 {round(py23-1.5,2)} 0) (effects (font (size 1.27 1.27))))\n'
        f'  (property "Value" "10k" (at 165 {round(py23+1.5,2)} 0) (effects (font (size 1.27 1.27))))\n'
        f'  (property "Footprint" "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal"'
        f' (at 165 {py23} 0) (effects (font (size 1.27 1.27)) (hide yes)))\n'
        f'  (property "Datasheet" "~" (at 165 {py23} 0) (effects (font (size 1.27 1.27)) (hide yes)))\n'
        f'  (pin "1" (uuid "{gen_uuid()}"))\n'
        f'  (pin "2" (uuid "{gen_uuid()}"))\n'
        f')'
    )
    elements.append(r3)
    elements.append(junction(157.7, py23))
    elements.append(wire(157.7, py23, 162.46, py23))
    elements.append(wire(167.54, py23, 172.0, py23))
    elements.append(global_label("+5V", 172.0, py23, 0))

    # R4 — 75Ω CLK series at (165, py22)
    r4 = (
        f'(symbol (lib_id "Device:R") (at 165 {py22} 0) (unit 1)\n'
        f'  (in_bom yes) (on_board yes) (dnp no) (uuid "{gen_uuid()}")\n'
        f'  (property "Reference" "R4" (at 165 {round(py22-1.5,2)} 0) (effects (font (size 1.27 1.27))))\n'
        f'  (property "Value" "75R" (at 165 {round(py22+1.5,2)} 0) (effects (font (size 1.27 1.27))))\n'
        f'  (property "Footprint" "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal"'
        f' (at 165 {py22} 0) (effects (font (size 1.27 1.27)) (hide yes)))\n'
        f'  (property "Datasheet" "~" (at 165 {py22} 0) (effects (font (size 1.27 1.27)) (hide yes)))\n'
        f'  (pin "1" (uuid "{gen_uuid()}"))\n'
        f'  (pin "2" (uuid "{gen_uuid()}"))\n'
        f')'
    )
    elements.append(r4)
    elements.append(junction(157.7, py22))
    elements.append(wire(157.7, py22, 162.46, py22))
    elements.append(wire(167.54, py22, 172.0, py22))
    elements.append(net_label("AY_CLK_SRC", 172.0, py22, 0))

    # =========================================================================
    # ARDUINO PRO MICRO SECTION
    # =========================================================================

    def u2_lpy(n):
        return round(151.03 + (n - 1) * 2.54, 2)

    def u2_rpy(n):
        return round(151.03 + (n - 13) * 2.54, 2)

    u2 = (
        f'(symbol (lib_id "Custom:Arduino_ProMicro") (at 240 165 0) (unit 1)\n'
        f'  (in_bom yes) (on_board yes) (dnp no) (uuid "{gen_uuid()}")\n'
        f'  (property "Reference" "U2" (at 242 163 0) (effects (font (size 1.27 1.27))))\n'
        f'  (property "Value" "Arduino_ProMicro" (at 242 165 0) (effects (font (size 1.27 1.27))))\n'
        f'  (property "Footprint" "Module:Arduino_Pro_Micro" (at 240 165 0)'
        f' (effects (font (size 1.27 1.27)) (hide yes)))\n'
        f'  (property "Datasheet" "~" (at 240 165 0)'
        f' (effects (font (size 1.27 1.27)) (hide yes)))\n'
    )
    for n in range(1, 25):
        u2 += f'  (pin "{n}" (uuid "{gen_uuid()}"))\n'
    u2 += ")"
    elements.append(u2)

    elements.append(no_connect(227.3, u2_lpy(1)))
    elements.append(wire(227.3, u2_lpy(2), 222.3, u2_lpy(2)))
    elements.append(net_label("MIDI_RX", 222.3, u2_lpy(2), 180))
    elements.append(wire(227.3, u2_lpy(3), 222.3, u2_lpy(3)))
    elements.append(global_label("GND", 222.3, u2_lpy(3), 180))
    elements.append(wire(227.3, u2_lpy(4), 222.3, u2_lpy(4)))
    elements.append(global_label("GND", 222.3, u2_lpy(4), 180))

    for pin_n, lname in {5:"DA0",6:"DA1",7:"DA2",8:"DA3",9:"DA4",10:"DA5",11:"DA6"}.items():
        py = u2_lpy(pin_n)
        elements.append(wire(227.3, py, 222.3, py))
        elements.append(net_label(lname, 222.3, py, 180))

    py_p12 = u2_lpy(12)
    elements.append(wire(227.3, py_p12, 222.3, py_p12))
    elements.append(net_label("AY_CLK_SRC", 222.3, py_p12, 180))

    elements.append(no_connect(252.7, u2_rpy(13)))
    elements.append(wire(252.7, u2_rpy(14), 257.7, u2_rpy(14)))
    elements.append(global_label("GND", 257.7, u2_rpy(14), 0))
    elements.append(no_connect(252.7, u2_rpy(15)))
    elements.append(wire(252.7, u2_rpy(16), 257.7, u2_rpy(16)))
    elements.append(global_label("+5V", 257.7, u2_rpy(16), 0))
    elements.append(wire(252.7, u2_rpy(17), 257.7, u2_rpy(17)))
    elements.append(net_label("GATE_IN", 257.7, u2_rpy(17), 0))
    elements.append(wire(252.7, u2_rpy(18), 257.7, u2_rpy(18)))
    elements.append(net_label("AY_BC2", 257.7, u2_rpy(18), 0))
    elements.append(wire(252.7, u2_rpy(19), 257.7, u2_rpy(19)))
    elements.append(net_label("CV_SCALED", 257.7, u2_rpy(19), 0))
    elements.append(wire(252.7, u2_rpy(20), 257.7, u2_rpy(20)))
    elements.append(net_label("AY_BDIR", 257.7, u2_rpy(20), 0))
    elements.append(wire(252.7, u2_rpy(21), 257.7, u2_rpy(21)))
    elements.append(net_label("AY_RST", 257.7, u2_rpy(21), 0))
    elements.append(no_connect(252.7, u2_rpy(22)))
    elements.append(wire(252.7, u2_rpy(23), 257.7, u2_rpy(23)))
    elements.append(net_label("AY_BDIR", 257.7, u2_rpy(23), 0))
    elements.append(wire(252.7, u2_rpy(24), 257.7, u2_rpy(24)))
    elements.append(net_label("DA7", 257.7, u2_rpy(24), 0))

    # =========================================================================
    # CV/GATE INPUT SECTION
    # =========================================================================

    j4 = (
        f'(symbol (lib_id "Connector_Audio:AudioJack2") (at 20 255 0) (unit 1)\n'
        f'  (in_bom yes) (on_board yes) (dnp no) (uuid "{gen_uuid()}")\n'
        f'  (property "Reference" "J4" (at 22 253 0) (effects (font (size 1.27 1.27))))\n'
        f'  (property "Value" "CV_IN" (at 22 255 0) (effects (font (size 1.27 1.27))))\n'
        f'  (property "Footprint" "Connector_Audio:Jack_3.5mm_PJ301M-12_Vertical"'
        f' (at 20 255 0) (effects (font (size 1.27 1.27)) (hide yes)))\n'
        f'  (property "Datasheet" "~" (at 20 255 0) (effects (font (size 1.27 1.27)) (hide yes)))\n'
        f'  (pin "1" (uuid "{gen_uuid()}"))\n'
        f'  (pin "2" (uuid "{gen_uuid()}"))\n'
        f')'
    )
    elements.append(j4)
    elements.append(wire(12.38, 255, 30.0, 255))
    elements.append(wire(27.62, 255, 30.0, 255))
    elements.append(wire(20, 257.54, 20, 261))
    elements.append(global_label("GND", 20, 261, 270))

    j5 = (
        f'(symbol (lib_id "Connector_Audio:AudioJack2") (at 20 280 0) (unit 1)\n'
        f'  (in_bom yes) (on_board yes) (dnp no) (uuid "{gen_uuid()}")\n'
        f'  (property "Reference" "J5" (at 22 278 0) (effects (font (size 1.27 1.27))))\n'
        f'  (property "Value" "GATE_IN" (at 22 280 0) (effects (font (size 1.27 1.27))))\n'
        f'  (property "Footprint" "Connector_Audio:Jack_3.5mm_PJ301M-12_Vertical"'
        f' (at 20 280 0) (effects (font (size 1.27 1.27)) (hide yes)))\n'
        f'  (property "Datasheet" "~" (at 20 280 0) (effects (font (size 1.27 1.27)) (hide yes)))\n'
        f'  (pin "1" (uuid "{gen_uuid()}"))\n'
        f'  (pin "2" (uuid "{gen_uuid()}"))\n'
        f')'
    )
    elements.append(j5)
    elements.append(wire(27.62, 280, 30.0, 280))
    elements.append(wire(20, 282.54, 20, 286))
    elements.append(global_label("GND", 20, 286, 270))

    # R5 — 100kΩ CV input to IN+
    r5 = (
        f'(symbol (lib_id "Device:R") (at 50 252 0) (unit 1)\n'
        f'  (in_bom yes) (on_board yes) (dnp no) (uuid "{gen_uuid()}")\n'
        f'  (property "Reference" "R5" (at 50 250.5 0) (effects (font (size 1.27 1.27))))\n'
        f'  (property "Value" "100k" (at 50 253.5 0) (effects (font (size 1.27 1.27))))\n'
        f'  (property "Footprint" "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal"'
        f' (at 50 252 0) (effects (font (size 1.27 1.27)) (hide yes)))\n'
        f'  (property "Datasheet" "~" (at 50 252 0) (effects (font (size 1.27 1.27)) (hide yes)))\n'
        f'  (pin "1" (uuid "{gen_uuid()}"))\n'
        f'  (pin "2" (uuid "{gen_uuid()}"))\n'
        f')'
    )
    elements.append(r5)
    elements.append(wire(30.0, 255, 47.46, 255))
    elements.append(wire(47.46, 255, 47.46, 252))
    elements.append(wire(52.54, 252, 70.0, 252))

    # R6 — 100kΩ IN+ to -12V
    r6 = (
        f'(symbol (lib_id "Device:R") (at 70 263 90) (unit 1)\n'
        f'  (in_bom yes) (on_board yes) (dnp no) (uuid "{gen_uuid()}")\n'
        f'  (property "Reference" "R6" (at 68.5 263 90) (effects (font (size 1.27 1.27))))\n'
        f'  (property "Value" "100k" (at 71.5 263 90) (effects (font (size 1.27 1.27))))\n'
        f'  (property "Footprint" "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal"'
        f' (at 70 263 0) (effects (font (size 1.27 1.27)) (hide yes)))\n'
        f'  (property "Datasheet" "~" (at 70 263 0) (effects (font (size 1.27 1.27)) (hide yes)))\n'
        f'  (pin "1" (uuid "{gen_uuid()}"))\n'
        f'  (pin "2" (uuid "{gen_uuid()}"))\n'
        f')'
    )
    elements.append(r6)
    elements.append(junction(70.0, 252.0))
    elements.append(wire(70.0, 252.0, 70.0, 260.46))
    elements.append(wire(70.0, 265.54, 70.0, 268.0))
    elements.append(global_label("-12V", 70.0, 268.0, 270))

    # U4 unit 1 — TL072 CV buffer at (85, 255)
    u4_unit1 = (
        f'(symbol (lib_id "Amplifier_Operational:TL072") (at 85 255 0) (unit 1)\n'
        f'  (in_bom yes) (on_board yes) (dnp no) (uuid "{gen_uuid()}")\n'
        f'  (property "Reference" "U4" (at 87 252 0) (effects (font (size 1.27 1.27))))\n'
        f'  (property "Value" "TL072" (at 87 254 0) (effects (font (size 1.27 1.27))))\n'
        f'  (property "Footprint" "Package_DIP:DIP-8_W7.62mm"'
        f' (at 85 255 0) (effects (font (size 1.27 1.27)) (hide yes)))\n'
        f'  (property "Datasheet" "~" (at 85 255 0) (effects (font (size 1.27 1.27)) (hide yes)))\n'
        f'  (pin "1" (uuid "{gen_uuid()}"))\n'
        f'  (pin "2" (uuid "{gen_uuid()}"))\n'
        f'  (pin "3" (uuid "{gen_uuid()}"))\n'
        f')'
    )
    elements.append(u4_unit1)
    # Connect R5/R6 junction to IN+ (pin 3 exits at -7.62,-2.54 from origin = 77.38,257.54)
    elements.append(wire(70.0, 252.0, 70.0, 257.54))
    elements.append(wire(70.0, 257.54, 77.38, 257.54))
    # Unity gain feedback: OUT(92.62,255) -> corner -> IN-(77.38,252.46)
    elements.append(wire(92.62, 255.0, 98.0, 255.0))
    elements.append(wire(98.0, 255.0, 98.0, 250.0))
    elements.append(wire(98.0, 250.0, 77.38, 250.0))
    elements.append(wire(77.38, 250.0, 77.38, 252.46))
    elements.append(junction(98.0, 255.0))
    # CV_SCALED net label at output
    elements.append(net_label("CV_SCALED", 98.0, 255.0, 0))

    # D3 — BAT42 clamp to +5V at (108, 250)
    d3 = (
        f'(symbol (lib_id "Device:D_Schottky") (at 108 250 0) (unit 1)\n'
        f'  (in_bom yes) (on_board yes) (dnp no) (uuid "{gen_uuid()}")\n'
        f'  (property "Reference" "D3" (at 108 248 0) (effects (font (size 1.27 1.27))))\n'
        f'  (property "Value" "BAT42" (at 108 251.5 0) (effects (font (size 1.27 1.27))))\n'
        f'  (property "Footprint" "Diode_THT:D_DO-35_SOD27_P7.62mm_Horizontal"'
        f' (at 108 250 0) (effects (font (size 1.27 1.27)) (hide yes)))\n'
        f'  (property "Datasheet" "~" (at 108 250 0) (effects (font (size 1.27 1.27)) (hide yes)))\n'
        f'  (pin "1" (uuid "{gen_uuid()}"))\n'
        f'  (pin "2" (uuid "{gen_uuid()}"))\n'
        f')'
    )
    elements.append(d3)
    elements.append(wire(98.0, 250.0, 105.46, 250.0))
    elements.append(wire(110.54, 250.0, 115.0, 250.0))
    elements.append(global_label("+5V", 115.0, 250.0, 0))

    # D4 — BAT42 clamp to GND at (108, 260)
    d4 = (
        f'(symbol (lib_id "Device:D_Schottky") (at 108 260 0) (unit 1)\n'
        f'  (in_bom yes) (on_board yes) (dnp no) (uuid "{gen_uuid()}")\n'
        f'  (property "Reference" "D4" (at 108 258 0) (effects (font (size 1.27 1.27))))\n'
        f'  (property "Value" "BAT42" (at 108 261.5 0) (effects (font (size 1.27 1.27))))\n'
        f'  (property "Footprint" "Diode_THT:D_DO-35_SOD27_P7.62mm_Horizontal"'
        f' (at 108 260 0) (effects (font (size 1.27 1.27)) (hide yes)))\n'
        f'  (property "Datasheet" "~" (at 108 260 0) (effects (font (size 1.27 1.27)) (hide yes)))\n'
        f'  (pin "1" (uuid "{gen_uuid()}"))\n'
        f'  (pin "2" (uuid "{gen_uuid()}"))\n'
        f')'
    )
    elements.append(d4)
    elements.append(wire(98.0, 255.0, 98.0, 260.0))
    elements.append(wire(98.0, 260.0, 105.46, 260.0))
    elements.append(wire(110.54, 260.0, 115.0, 260.0))
    elements.append(global_label("GND", 115.0, 260.0, 0))

    # R7 — 100kΩ gate divider top at (50, 278)
    r7 = (
        f'(symbol (lib_id "Device:R") (at 50 278 0) (unit 1)\n'
        f'  (in_bom yes) (on_board yes) (dnp no) (uuid "{gen_uuid()}")\n'
        f'  (property "Reference" "R7" (at 50 276.5 0) (effects (font (size 1.27 1.27))))\n'
        f'  (property "Value" "100k" (at 50 279.5 0) (effects (font (size 1.27 1.27))))\n'
        f'  (property "Footprint" "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal"'
        f' (at 50 278 0) (effects (font (size 1.27 1.27)) (hide yes)))\n'
        f'  (property "Datasheet" "~" (at 50 278 0) (effects (font (size 1.27 1.27)) (hide yes)))\n'
        f'  (pin "1" (uuid "{gen_uuid()}"))\n'
        f'  (pin "2" (uuid "{gen_uuid()}"))\n'
        f')'
    )
    elements.append(r7)
    elements.append(wire(27.62, 280.0, 47.46, 280.0))
    elements.append(wire(47.46, 280.0, 47.46, 278.0))
    elements.append(wire(52.54, 278.0, 70.0, 278.0))
    elements.append(junction(70.0, 278.0))
    elements.append(net_label("GATE_IN", 70.0, 278.0, 0))

    # R8 — 100kΩ gate divider bottom at (70, 285)
    r8 = (
        f'(symbol (lib_id "Device:R") (at 70 285 90) (unit 1)\n'
        f'  (in_bom yes) (on_board yes) (dnp no) (uuid "{gen_uuid()}")\n'
        f'  (property "Reference" "R8" (at 68.5 285 90) (effects (font (size 1.27 1.27))))\n'
        f'  (property "Value" "100k" (at 71.5 285 90) (effects (font (size 1.27 1.27))))\n'
        f'  (property "Footprint" "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal"'
        f' (at 70 285 0) (effects (font (size 1.27 1.27)) (hide yes)))\n'
        f'  (property "Datasheet" "~" (at 70 285 0) (effects (font (size 1.27 1.27)) (hide yes)))\n'
        f'  (pin "1" (uuid "{gen_uuid()}"))\n'
        f'  (pin "2" (uuid "{gen_uuid()}"))\n'
        f')'
    )
    elements.append(r8)
    elements.append(wire(70.0, 278.0, 70.0, 282.46))
    elements.append(wire(70.0, 287.54, 70.0, 291.0))
    elements.append(global_label("GND", 70.0, 291.0, 270))

    # U4 unit 3 — power pins at (85, 240)
    u4_unit3 = (
        f'(symbol (lib_id "Amplifier_Operational:TL072") (at 85 240 0) (unit 3)\n'
        f'  (in_bom yes) (on_board yes) (dnp no) (uuid "{gen_uuid()}")\n'
        f'  (property "Reference" "U4" (at 87 238 0) (effects (font (size 1.27 1.27))))\n'
        f'  (property "Value" "TL072" (at 87 240 0) (effects (font (size 1.27 1.27))))\n'
        f'  (property "Footprint" "Package_DIP:DIP-8_W7.62mm"'
        f' (at 85 240 0) (effects (font (size 1.27 1.27)) (hide yes)))\n'
        f'  (property "Datasheet" "~" (at 85 240 0) (effects (font (size 1.27 1.27)) (hide yes)))\n'
        f'  (pin "4" (uuid "{gen_uuid()}"))\n'
        f'  (pin "8" (uuid "{gen_uuid()}"))\n'
        f')'
    )
    elements.append(u4_unit3)
    elements.append(wire(85.0, 237.46, 85.0, 235.0))
    elements.append(global_label("+12V", 85.0, 235.0, 90))
    elements.append(wire(85.0, 242.54, 85.0, 245.0))
    elements.append(global_label("-12V", 85.0, 245.0, 270))

    # =========================================================================
    # AUDIO OUTPUT SECTION
    # =========================================================================

    # U4 unit 2 — TL072 audio summer at (230, 260)
    u4_unit2 = (
        f'(symbol (lib_id "Amplifier_Operational:TL072") (at 230 260 0) (unit 2)\n'
        f'  (in_bom yes) (on_board yes) (dnp no) (uuid "{gen_uuid()}")\n'
        f'  (property "Reference" "U4" (at 232 257 0) (effects (font (size 1.27 1.27))))\n'
        f'  (property "Value" "TL072" (at 232 259 0) (effects (font (size 1.27 1.27))))\n'
        f'  (property "Footprint" "Package_DIP:DIP-8_W7.62mm"'
        f' (at 230 260 0) (effects (font (size 1.27 1.27)) (hide yes)))\n'
        f'  (property "Datasheet" "~" (at 230 260 0) (effects (font (size 1.27 1.27)) (hide yes)))\n'
        f'  (pin "5" (uuid "{gen_uuid()}"))\n'
        f'  (pin "6" (uuid "{gen_uuid()}"))\n'
        f'  (pin "7" (uuid "{gen_uuid()}"))\n'
        f')'
    )
    elements.append(u4_unit2)
    # IN+ (pin 7) exits at -7.62,-2.54 from (230,260) = (222.38,262.54) -> GND
    elements.append(wire(222.38, 262.54, 218.0, 262.54))
    elements.append(global_label("GND", 218.0, 262.54, 180))

    sum_node_x, sum_node_y = 210.0, 257.46   # summing junction at IN- (pin 6)

    # R9 — AoutA 100kΩ
    r9 = (
        f'(symbol (lib_id "Device:R") (at 200 255 0) (unit 1)\n'
        f'  (in_bom yes) (on_board yes) (dnp no) (uuid "{gen_uuid()}")\n'
        f'  (property "Reference" "R9" (at 200 253.5 0) (effects (font (size 1.27 1.27))))\n'
        f'  (property "Value" "100k" (at 200 256.5 0) (effects (font (size 1.27 1.27))))\n'
        f'  (property "Footprint" "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal"'
        f' (at 200 255 0) (effects (font (size 1.27 1.27)) (hide yes)))\n'
        f'  (property "Datasheet" "~" (at 200 255 0) (effects (font (size 1.27 1.27)) (hide yes)))\n'
        f'  (pin "1" (uuid "{gen_uuid()}"))\n'
        f'  (pin "2" (uuid "{gen_uuid()}"))\n'
        f')'
    )
    elements.append(r9)
    elements.append(net_label("AY_AOUT_A", 195.0, 255.0, 180))
    elements.append(wire(195.0, 255.0, 197.46, 255.0))
    elements.append(wire(202.54, 255.0, sum_node_x, 255.0))
    elements.append(wire(sum_node_x, 255.0, sum_node_x, sum_node_y))

    # R10 — AoutB 100kΩ
    r10 = (
        f'(symbol (lib_id "Device:R") (at 200 260 0) (unit 1)\n'
        f'  (in_bom yes) (on_board yes) (dnp no) (uuid "{gen_uuid()}")\n'
        f'  (property "Reference" "R10" (at 200 258.5 0) (effects (font (size 1.27 1.27))))\n'
        f'  (property "Value" "100k" (at 200 261.5 0) (effects (font (size 1.27 1.27))))\n'
        f'  (property "Footprint" "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal"'
        f' (at 200 260 0) (effects (font (size 1.27 1.27)) (hide yes)))\n'
        f'  (property "Datasheet" "~" (at 200 260 0) (effects (font (size 1.27 1.27)) (hide yes)))\n'
        f'  (pin "1" (uuid "{gen_uuid()}"))\n'
        f'  (pin "2" (uuid "{gen_uuid()}"))\n'
        f')'
    )
    elements.append(r10)
    elements.append(net_label("AY_AOUT_B", 195.0, 260.0, 180))
    elements.append(wire(195.0, 260.0, 197.46, 260.0))
    elements.append(wire(202.54, 260.0, sum_node_x, 260.0))
    elements.append(wire(sum_node_x, 260.0, sum_node_x, sum_node_y))
    elements.append(junction(sum_node_x, sum_node_y))

    # R11 — AoutC 100kΩ
    r11 = (
        f'(symbol (lib_id "Device:R") (at 200 265 0) (unit 1)\n'
        f'  (in_bom yes) (on_board yes) (dnp no) (uuid "{gen_uuid()}")\n'
        f'  (property "Reference" "R11" (at 200 263.5 0) (effects (font (size 1.27 1.27))))\n'
        f'  (property "Value" "100k" (at 200 266.5 0) (effects (font (size 1.27 1.27))))\n'
        f'  (property "Footprint" "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal"'
        f' (at 200 265 0) (effects (font (size 1.27 1.27)) (hide yes)))\n'
        f'  (property "Datasheet" "~" (at 200 265 0) (effects (font (size 1.27 1.27)) (hide yes)))\n'
        f'  (pin "1" (uuid "{gen_uuid()}"))\n'
        f'  (pin "2" (uuid "{gen_uuid()}"))\n'
        f')'
    )
    elements.append(r11)
    elements.append(net_label("AY_AOUT_C", 195.0, 265.0, 180))
    elements.append(wire(195.0, 265.0, 197.46, 265.0))
    elements.append(wire(202.54, 265.0, sum_node_x, 265.0))
    elements.append(wire(sum_node_x, 265.0, sum_node_x, sum_node_y))
    # Wire summing junction to U4B IN- (222.38, 257.46)
    elements.append(wire(sum_node_x, sum_node_y, 222.38, sum_node_y))

    # R12 — 100kΩ feedback
    r12 = (
        f'(symbol (lib_id "Device:R") (at 230 248 0) (unit 1)\n'
        f'  (in_bom yes) (on_board yes) (dnp no) (uuid "{gen_uuid()}")\n'
        f'  (property "Reference" "R12" (at 230 246.5 0) (effects (font (size 1.27 1.27))))\n'
        f'  (property "Value" "100k" (at 230 249.5 0) (effects (font (size 1.27 1.27))))\n'
        f'  (property "Footprint" "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal"'
        f' (at 230 248 0) (effects (font (size 1.27 1.27)) (hide yes)))\n'
        f'  (property "Datasheet" "~" (at 230 248 0) (effects (font (size 1.27 1.27)) (hide yes)))\n'
        f'  (pin "1" (uuid "{gen_uuid()}"))\n'
        f'  (pin "2" (uuid "{gen_uuid()}"))\n'
        f')'
    )
    elements.append(r12)
    out_x, out_y = 237.62, 260.0   # U4B OUT pin
    # R12 pin 1 connects to summing node via upward wire
    elements.append(wire(sum_node_x, sum_node_y, sum_node_x, 248.0))
    elements.append(wire(sum_node_x, 248.0, 227.46, 248.0))
    # R12 pin 2 connects to output
    elements.append(wire(232.54, 248.0, out_x, 248.0))
    elements.append(wire(out_x, 248.0, out_x, out_y))
    elements.append(junction(out_x, out_y))

    # C9 — 4.7nF LP filter cap at (255, 248)
    c9 = (
        f'(symbol (lib_id "Device:C") (at 255 248 0) (unit 1)\n'
        f'  (in_bom yes) (on_board yes) (dnp no) (uuid "{gen_uuid()}")\n'
        f'  (property "Reference" "C9" (at 255 246.5 0) (effects (font (size 1.27 1.27))))\n'
        f'  (property "Value" "4.7nF" (at 255 249.5 0) (effects (font (size 1.27 1.27))))\n'
        f'  (property "Footprint" "Capacitor_THT:C_Disc_D4.7mm_W2.5mm_P5.00mm"'
        f' (at 255 248 0) (effects (font (size 1.27 1.27)) (hide yes)))\n'
        f'  (property "Datasheet" "~" (at 255 248 0) (effects (font (size 1.27 1.27)) (hide yes)))\n'
        f'  (pin "1" (uuid "{gen_uuid()}"))\n'
        f'  (pin "2" (uuid "{gen_uuid()}"))\n'
        f')'
    )
    elements.append(c9)
    elements.append(wire(out_x, out_y, 248.0, out_y))
    elements.append(wire(248.0, out_y, 248.0, 248.0))
    elements.append(wire(248.0, 248.0, 252.46, 248.0))
    elements.append(junction(248.0, out_y))
    elements.append(wire(257.54, 248.0, 262.0, 248.0))
    elements.append(global_label("GND", 262.0, 248.0, 0))

    # R13 — 4.7kΩ output load at (265, 260)
    r13 = (
        f'(symbol (lib_id "Device:R") (at 265 260 90) (unit 1)\n'
        f'  (in_bom yes) (on_board yes) (dnp no) (uuid "{gen_uuid()}")\n'
        f'  (property "Reference" "R13" (at 263.5 260 90) (effects (font (size 1.27 1.27))))\n'
        f'  (property "Value" "4.7k" (at 266.5 260 90) (effects (font (size 1.27 1.27))))\n'
        f'  (property "Footprint" "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal"'
        f' (at 265 260 0) (effects (font (size 1.27 1.27)) (hide yes)))\n'
        f'  (property "Datasheet" "~" (at 265 260 0) (effects (font (size 1.27 1.27)) (hide yes)))\n'
        f'  (pin "1" (uuid "{gen_uuid()}"))\n'
        f'  (pin "2" (uuid "{gen_uuid()}"))\n'
        f')'
    )
    elements.append(r13)
    elements.append(wire(248.0, out_y, 265.0, out_y))
    elements.append(junction(248.0, out_y))
    elements.append(wire(265.0, out_y, 265.0, 257.46))
    elements.append(wire(265.0, 262.54, 265.0, 266.0))
    elements.append(global_label("GND", 265.0, 266.0, 270))

    # C10 — 1µF DC blocking at (285, 260)
    c10 = (
        f'(symbol (lib_id "Device:C_Polarized") (at 285 260 0) (unit 1)\n'
        f'  (in_bom yes) (on_board yes) (dnp no) (uuid "{gen_uuid()}")\n'
        f'  (property "Reference" "C10" (at 285 258.5 0) (effects (font (size 1.27 1.27))))\n'
        f'  (property "Value" "1uF" (at 285 261.5 0) (effects (font (size 1.27 1.27))))\n'
        f'  (property "Footprint" "Capacitor_THT:CP_Radial_D5.0mm_P2.50mm"'
        f' (at 285 260 0) (effects (font (size 1.27 1.27)) (hide yes)))\n'
        f'  (property "Datasheet" "~" (at 285 260 0) (effects (font (size 1.27 1.27)) (hide yes)))\n'
        f'  (pin "1" (uuid "{gen_uuid()}"))\n'
        f'  (pin "2" (uuid "{gen_uuid()}"))\n'
        f')'
    )
    elements.append(c10)
    elements.append(junction(265.0, out_y))
    elements.append(wire(265.0, out_y, 282.46, out_y))

    # R14 — 1kΩ output impedance at (310, 258)
    r14 = (
        f'(symbol (lib_id "Device:R") (at 310 258 90) (unit 1)\n'
        f'  (in_bom yes) (on_board yes) (dnp no) (uuid "{gen_uuid()}")\n'
        f'  (property "Reference" "R14" (at 308.5 258 90) (effects (font (size 1.27 1.27))))\n'
        f'  (property "Value" "1k" (at 311.5 258 90) (effects (font (size 1.27 1.27))))\n'
        f'  (property "Footprint" "Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal"'
        f' (at 310 258 0) (effects (font (size 1.27 1.27)) (hide yes)))\n'
        f'  (property "Datasheet" "~" (at 310 258 0) (effects (font (size 1.27 1.27)) (hide yes)))\n'
        f'  (pin "1" (uuid "{gen_uuid()}"))\n'
        f'  (pin "2" (uuid "{gen_uuid()}"))\n'
        f')'
    )
    elements.append(r14)
    elements.append(wire(287.54, out_y, 310.0, out_y))
    elements.append(junction(310.0, out_y))
    elements.append(wire(310.0, out_y, 310.0, 255.46))
    elements.append(wire(310.0, 260.54, 310.0, 264.0))
    elements.append(global_label("GND", 310.0, 264.0, 270))

    # J3 — Audio output jack at (325, 260)
    j3 = (
        f'(symbol (lib_id "Connector_Audio:AudioJack2") (at 325 260 0) (unit 1)\n'
        f'  (in_bom yes) (on_board yes) (dnp no) (uuid "{gen_uuid()}")\n'
        f'  (property "Reference" "J3" (at 327 258 0) (effects (font (size 1.27 1.27))))\n'
        f'  (property "Value" "AUDIO_OUT" (at 327 260 0) (effects (font (size 1.27 1.27))))\n'
        f'  (property "Footprint" "Connector_Audio:Jack_3.5mm_PJ301M-12_Vertical"'
        f' (at 325 260 0) (effects (font (size 1.27 1.27)) (hide yes)))\n'
        f'  (property "Datasheet" "~" (at 325 260 0) (effects (font (size 1.27 1.27)) (hide yes)))\n'
        f'  (pin "1" (uuid "{gen_uuid()}"))\n'
        f'  (pin "2" (uuid "{gen_uuid()}"))\n'
        f')'
    )
    elements.append(j3)
    elements.append(wire(310.0, out_y, 317.38, out_y))
    elements.append(wire(325.0, 262.54, 325.0, 266.0))
    elements.append(global_label("GND", 325.0, 266.0, 270))

    return "\n".join(elements)


if __name__ == "__main__":
    print(get_main_circuit_elements())
