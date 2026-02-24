#!/usr/bin/env python3
"""AY-3-8910 Eurorack module — KiCad netlist via skidl."""

import os
from skidl import *

SYM = "/usr/share/kicad/symbols"

# ─── Custom part templates ─────────────────────────────────────────────────────

def make_ay3_8910():
    """AY-3-8910 PSG, 40-pin DIP.

    Datasheet pin map:
      1  GND      21 DA7(nc→datasheet pin ordering corrected below)
      2  NC       22 CLK
      3  AoutB    23 RESET
      4  AoutA    24 A9
      5  IOB7     25 A8
      6  IOB6     26 TEST2
      7  IOB5     27 BDIR
      8  IOB4     28 BC2
      9  IOB3     29 BC1
     10  IOB2     30 DA7
     11  IOB1     31 DA6
     12  IOB0     32 DA5
     13  IOA7     33 DA4
     14  IOA6     34 DA3
     15  IOA5     35 DA2
     16  IOA4     36 DA1
     17  IOA3     37 DA0
     18  IOA2     38 AoutC
     19  IOA1     39 TEST1
     20  IOA0     40 VCC
    """
    p = Part(tool=SKIDL, name="AY-3-8910",
             footprint="Package_DIP:DIP-40_W15.24mm", dest=TEMPLATE)
    p += Pin(num=1,  name="GND",   func=Pin.types.PWRIN)
    p += Pin(num=2,  name="NC",    func=Pin.types.NOCONNECT)
    p += Pin(num=3,  name="AoutB", func=Pin.types.OUTPUT)
    p += Pin(num=4,  name="AoutA", func=Pin.types.OUTPUT)
    p += Pin(num=5,  name="IOB7",  func=Pin.types.BIDIR)
    p += Pin(num=6,  name="IOB6",  func=Pin.types.BIDIR)
    p += Pin(num=7,  name="IOB5",  func=Pin.types.BIDIR)
    p += Pin(num=8,  name="IOB4",  func=Pin.types.BIDIR)
    p += Pin(num=9,  name="IOB3",  func=Pin.types.BIDIR)
    p += Pin(num=10, name="IOB2",  func=Pin.types.BIDIR)
    p += Pin(num=11, name="IOB1",  func=Pin.types.BIDIR)
    p += Pin(num=12, name="IOB0",  func=Pin.types.BIDIR)
    p += Pin(num=13, name="IOA7",  func=Pin.types.BIDIR)
    p += Pin(num=14, name="IOA6",  func=Pin.types.BIDIR)
    p += Pin(num=15, name="IOA5",  func=Pin.types.BIDIR)
    p += Pin(num=16, name="IOA4",  func=Pin.types.BIDIR)
    p += Pin(num=17, name="IOA3",  func=Pin.types.BIDIR)
    p += Pin(num=18, name="IOA2",  func=Pin.types.BIDIR)
    p += Pin(num=19, name="IOA1",  func=Pin.types.BIDIR)
    p += Pin(num=20, name="IOA0",  func=Pin.types.BIDIR)
    p += Pin(num=21, name="DA7",   func=Pin.types.BIDIR)   # datasheet: NC on some variants; actual DA7 here
    p += Pin(num=22, name="CLK",   func=Pin.types.INPUT)
    p += Pin(num=23, name="RESET", func=Pin.types.INPUT)
    p += Pin(num=24, name="A9",    func=Pin.types.INPUT)
    p += Pin(num=25, name="A8",    func=Pin.types.INPUT)
    p += Pin(num=26, name="TEST2", func=Pin.types.NOCONNECT)
    p += Pin(num=27, name="BDIR",  func=Pin.types.INPUT)
    p += Pin(num=28, name="BC2",   func=Pin.types.INPUT)
    p += Pin(num=29, name="BC1",   func=Pin.types.INPUT)
    p += Pin(num=30, name="DA7",   func=Pin.types.BIDIR)
    p += Pin(num=31, name="DA6",   func=Pin.types.BIDIR)
    p += Pin(num=32, name="DA5",   func=Pin.types.BIDIR)
    p += Pin(num=33, name="DA4",   func=Pin.types.BIDIR)
    p += Pin(num=34, name="DA3",   func=Pin.types.BIDIR)
    p += Pin(num=35, name="DA2",   func=Pin.types.BIDIR)
    p += Pin(num=36, name="DA1",   func=Pin.types.BIDIR)
    p += Pin(num=37, name="DA0",   func=Pin.types.BIDIR)
    p += Pin(num=38, name="AoutC", func=Pin.types.OUTPUT)
    p += Pin(num=39, name="TEST1", func=Pin.types.NOCONNECT)
    p += Pin(num=40, name="VCC",   func=Pin.types.PWRIN)
    return p


def make_arduino_promicro():
    """Arduino Pro Micro (ATmega32U4, 5V/16MHz)."""
    p = Part(tool=SKIDL, name="Arduino_ProMicro",
             footprint="Module:Arduino_Pro_Micro", dest=TEMPLATE)
    p += Pin(num=1,  name="TX",   func=Pin.types.OUTPUT)
    p += Pin(num=2,  name="RX",   func=Pin.types.INPUT)
    p += Pin(num=3,  name="GND",  func=Pin.types.PWRIN)
    p += Pin(num=4,  name="GND2", func=Pin.types.PWRIN)
    p += Pin(num=5,  name="D2",   func=Pin.types.BIDIR)
    p += Pin(num=6,  name="D3",   func=Pin.types.BIDIR)
    p += Pin(num=7,  name="D4",   func=Pin.types.BIDIR)
    p += Pin(num=8,  name="D5",   func=Pin.types.BIDIR)
    p += Pin(num=9,  name="D6",   func=Pin.types.BIDIR)
    p += Pin(num=10, name="D7",   func=Pin.types.BIDIR)
    p += Pin(num=11, name="D8",   func=Pin.types.BIDIR)
    p += Pin(num=12, name="D9",   func=Pin.types.BIDIR)
    p += Pin(num=13, name="D10",  func=Pin.types.BIDIR)
    p += Pin(num=14, name="D16",  func=Pin.types.BIDIR)  # MOSI / A2
    p += Pin(num=15, name="D14",  func=Pin.types.BIDIR)  # MISO / A0
    p += Pin(num=16, name="D15",  func=Pin.types.BIDIR)  # SCK
    p += Pin(num=17, name="A1",   func=Pin.types.BIDIR)
    p += Pin(num=18, name="A3",   func=Pin.types.BIDIR)
    p += Pin(num=19, name="VCC",  func=Pin.types.PWRIN)
    p += Pin(num=20, name="RAW",  func=Pin.types.PWRIN)
    return p


# ─── Build circuit ─────────────────────────────────────────────────────────────

def ay_module():

    # Power nets
    vcc  = Net("+5V");  vcc.drive  = POWER
    v12  = Net("+12V"); v12.drive  = POWER
    vm12 = Net("-12V"); vm12.drive = POWER
    gnd  = Net("GND");  gnd.drive  = POWER

    # Internal signal nets
    v12r      = Net("+12V_RECT")
    midi_cur  = Net("MIDI_CUR")
    midi_a    = Net("MIDI_A")
    midi_rx   = Net("MIDI_RX")
    ay_clk    = Net("AY_CLK")
    clk_src   = Net("CLK_SRC")
    ay_rst    = Net("AY_RST")
    ay_bdir   = Net("AY_BDIR")
    ay_bc2    = Net("AY_BC2")
    da        = [Net(f"DA{i}") for i in range(8)]
    aout_a    = Net("AY_AOUT_A")
    aout_b    = Net("AY_AOUT_B")
    aout_c    = Net("AY_AOUT_C")
    cv_raw    = Net("CV_RAW")
    cv_mid    = Net("CV_MID")
    cv_out    = Net("CV_AMP_OUT")
    cv_in     = Net("CV_SCALED")
    gate_raw  = Net("GATE_RAW")
    gate_in   = Net("GATE_IN")
    inv_in    = Net("INV_IN")
    audio_sum = Net("AUDIO_SUM")
    audio_out = Net("AUDIO_OUT")

    # ── Power ──────────────────────────────────────────────────────────────────

    # J1: Eurorack 16-pin IDC  (2×8, odd/even numbering)
    J1 = Part(f"{SYM}/Connector_Generic.kicad_sym", "Conn_02x08_Odd_Even",
              footprint="Connector_IDC:IDC-Header_2x08_P2.54mm_Vertical",
              ref="J1", value="Eurorack_PWR")
    J1["Pin_1"]  += v12
    J1["Pin_3"]  += v12
    J1["Pin_2"]  += gnd
    J1["Pin_4"]  += gnd
    J1["Pin_6"]  += gnd
    J1["Pin_8"]  += gnd
    J1["Pin_10"] += gnd
    J1["Pin_12"] += gnd
    J1["Pin_14"] += vm12
    J1["Pin_16"] += vm12
    # +5V rail from bus not used (we regulate our own)
    J1["Pin_5"]  += NC
    J1["Pin_7"]  += NC
    J1["Pin_9"]  += NC
    J1["Pin_11"] += NC
    J1["Pin_13"] += NC
    J1["Pin_15"] += NC

    # D1: 1N4001 reverse-polarity protection on +12V
    D1 = Part(f"{SYM}/Device.kicad_sym", "D",
              footprint="Diode_THT:D_DO-41_SOD81_P10.16mm_Horizontal",
              ref="D1", value="1N4001")
    D1["A"] += v12
    D1["K"] += v12r

    # U5: LM7805 +5V regulator  (pins: 1=VI, 2=GND, 3=VO)
    U5 = Part(f"{SYM}/Regulator_Linear.kicad_sym", "LM7805_TO220",
              footprint="Package_TO_SOT_THT:TO-220-3_Vertical",
              ref="U5", value="LM7805")
    U5["VI"]  += v12r
    U5["GND"] += gnd
    U5["VO"]  += vcc

    C5 = Part(f"{SYM}/Device.kicad_sym", "C_Polarized",
              footprint="Capacitor_THT:CP_Radial_D6.3mm_P2.50mm",
              ref="C5", value="10µF")
    C5[1] += v12r; C5[2] += gnd

    C6 = Part(f"{SYM}/Device.kicad_sym", "C_Polarized",
              footprint="Capacitor_THT:CP_Radial_D6.3mm_P2.50mm",
              ref="C6", value="10µF")
    C6[1] += vcc; C6[2] += gnd

    C7 = Part(f"{SYM}/Device.kicad_sym", "C",
              footprint="Capacitor_THT:C_Disc_D5.0mm_W2.5mm_P5.00mm",
              ref="C7", value="100nF")
    C7[1] += vcc; C7[2] += gnd

    C8 = Part(f"{SYM}/Device.kicad_sym", "C",
              footprint="Capacitor_THT:C_Disc_D5.0mm_W2.5mm_P5.00mm",
              ref="C8", value="100nF")
    C8[1] += vcc; C8[2] += gnd

    # ── MIDI input ─────────────────────────────────────────────────────────────

    # J2: 5-pin DIN MIDI connector  (pins 1-5, all unnamed '~')
    J2 = Part(f"{SYM}/Connector.kicad_sym", "DIN-5",
              footprint="Connector_DIN:DIN5_262degree_Vertical",
              ref="J2", value="MIDI_IN")
    J2[4] += midi_cur
    J2[5] += gnd
    J2[1] += NC
    J2[2] += NC
    J2[3] += NC

    # R1: 220Ω MIDI current limit
    R1 = Part(f"{SYM}/Device.kicad_sym", "R",
              footprint="Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal",
              ref="R1", value="220R")
    R1[1] += midi_cur; R1[2] += midi_a

    # D2: 1N4148 transient protection
    D2 = Part(f"{SYM}/Device.kicad_sym", "D",
              footprint="Diode_THT:D_DO-35_SOD27_P7.62mm_Horizontal",
              ref="D2", value="1N4148")
    D2["A"] += midi_a; D2["K"] += vcc

    # U3: 6N137 optocoupler  (pins: NC,A,C,NC,VCC,GND,EN,VO by num 1..8)
    U3 = Part(f"{SYM}/Isolator.kicad_sym", "6N137",
              footprint="Package_DIP:DIP-8_W7.62mm",
              ref="U3", value="6N137")
    U3["A"]   += midi_a
    U3["C"]   += gnd
    U3["VCC"] += vcc
    U3["GND"] += gnd
    U3["EN"]  += vcc
    U3["NC"]  += NC

    # R2: 10kΩ pull-up on optocoupler output
    R2 = Part(f"{SYM}/Device.kicad_sym", "R",
              footprint="Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal",
              ref="R2", value="10k")
    R2[1] += vcc; R2[2] += midi_rx
    U3["VO"] += midi_rx

    # ── AY-3-8910 ──────────────────────────────────────────────────────────────

    U1 = make_ay3_8910()(ref="U1", value="AY-3-8910")
    U1["VCC"]   += vcc
    U1["GND"]   += gnd
    U1["CLK"]   += ay_clk
    U1["RESET"] += ay_rst
    U1["BDIR"]  += ay_bdir
    U1["BC2"]   += ay_bc2
    U1["BC1"]   += gnd      # simplified control: BC1 tied low
    U1["A8"]    += gnd
    U1["A9"]    += vcc
    U1["TEST1"] += NC
    U1["TEST2"] += NC
    # Data bus by pin number (DA0=37, DA1=36...DA7=30)
    U1[37] += da[0]
    U1[36] += da[1]
    U1[35] += da[2]
    U1[34] += da[3]
    U1[33] += da[4]
    U1[32] += da[5]
    U1[31] += da[6]
    U1[30] += da[7]
    U1["AoutA"] += aout_a
    U1["AoutB"] += aout_b
    U1["AoutC"] += aout_c
    for io in ["IOA0","IOA1","IOA2","IOA3","IOA4","IOA5","IOA6","IOA7",
               "IOB0","IOB1","IOB2","IOB3","IOB4","IOB5","IOB6","IOB7"]:
        U1[io] += NC

    # C9: 100nF VCC bypass for U1
    C9 = Part(f"{SYM}/Device.kicad_sym", "C",
              footprint="Capacitor_THT:C_Disc_D5.0mm_W2.5mm_P5.00mm",
              ref="C9", value="100nF")
    C9[1] += vcc; C9[2] += gnd

    # R3: 10kΩ RESET pull-up
    R3 = Part(f"{SYM}/Device.kicad_sym", "R",
              footprint="Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal",
              ref="R3", value="10k")
    R3[1] += vcc; R3[2] += ay_rst

    # R4: 75Ω CLK series resistor
    R4 = Part(f"{SYM}/Device.kicad_sym", "R",
              footprint="Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal",
              ref="R4", value="75R")
    R4[1] += clk_src; R4[2] += ay_clk

    # ── Arduino Pro Micro ──────────────────────────────────────────────────────

    U2 = make_arduino_promicro()(ref="U2", value="Arduino_ProMicro")
    U2["VCC"]  += vcc
    U2["GND"]  += gnd
    U2["GND2"] += gnd
    U2["RAW"]  += NC
    U2["RX"]   += midi_rx
    U2["D2"]   += da[0]
    U2["D3"]   += da[1]
    U2["D4"]   += da[2]
    U2["D5"]   += da[3]
    U2["D6"]   += da[4]
    U2["D7"]   += da[5]
    U2["D8"]   += da[6]
    U2["D10"]  += da[7]
    U2["D9"]   += clk_src
    U2["D14"]  += ay_bdir   # MISO/A0
    U2["D15"]  += ay_rst    # SCK
    U2["D16"]  += ay_bc2    # MOSI/A2
    U2["A1"]   += cv_in
    U2["A3"]   += gate_in

    # ── TL072 dual op-amp (U4) ─────────────────────────────────────────────────
    # Pin map: 3(+A), 2(-A), 1(outA), 5(+B), 6(-B), 7(outB), 8(V+), 4(V-)

    U4 = Part(f"{SYM}/Amplifier_Operational.kicad_sym", "TL072",
              footprint="Package_DIP:DIP-8_W7.62mm",
              ref="U4", value="TL072")
    U4[8] += v12    # V+
    U4[4] += vm12   # V-

    # Unit A: CV level-shift unity-gain buffer
    U4[3] += cv_mid        # non-inverting input
    U4[2] += cv_out        # inverting input tied to output (follower)
    U4[1] += cv_out        # output

    # Unit B: audio inverting summer
    U4[5] += gnd           # non-inverting input
    U4[6] += inv_in        # inverting input (summing node)
    U4[7] += audio_sum     # output

    # ── CV input ───────────────────────────────────────────────────────────────

    J4 = Part(f"{SYM}/Connector_Audio.kicad_sym", "AudioJack2",
              footprint="Connector_Audio:Jack_3.5mm_QingPu_WQP-PJ301BM_Vertical_CircularHoles",
              ref="J4", value="CV_IN")
    J4["S"] += gnd      # sleeve
    J4["T"] += cv_raw   # tip

    # R5, R6: 100k+100k level-shift divider (±5V input → ~0-5V)
    R5 = Part(f"{SYM}/Device.kicad_sym", "R",
              footprint="Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal",
              ref="R5", value="100k")
    R6 = Part(f"{SYM}/Device.kicad_sym", "R",
              footprint="Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal",
              ref="R6", value="100k")
    R5[1] += cv_raw; R5[2] += cv_mid
    R6[1] += cv_mid; R6[2] += vm12

    # D3, D4: BAT42 clamp diodes on op-amp output (0V / +5V)
    D3 = Part(f"{SYM}/Device.kicad_sym", "D_Schottky",
              footprint="Diode_THT:D_DO-35_SOD27_P7.62mm_Horizontal",
              ref="D3", value="BAT42")
    D4 = Part(f"{SYM}/Device.kicad_sym", "D_Schottky",
              footprint="Diode_THT:D_DO-35_SOD27_P7.62mm_Horizontal",
              ref="D4", value="BAT42")
    D3["A"] += gnd;   D3["K"] += cv_out    # low clamp
    D4["A"] += cv_out; D4["K"] += vcc      # high clamp

    C10 = Part(f"{SYM}/Device.kicad_sym", "C",
               footprint="Capacitor_THT:C_Disc_D5.0mm_W2.5mm_P5.00mm",
               ref="C10", value="100nF")
    C10[1] += cv_out; C10[2] += gnd
    cv_out += cv_in

    # ── Gate input ─────────────────────────────────────────────────────────────

    J5 = Part(f"{SYM}/Connector_Audio.kicad_sym", "AudioJack2",
              footprint="Connector_Audio:Jack_3.5mm_QingPu_WQP-PJ301BM_Vertical_CircularHoles",
              ref="J5", value="GATE_IN")
    J5["S"] += gnd
    J5["T"] += gate_raw

    R7 = Part(f"{SYM}/Device.kicad_sym", "R",
              footprint="Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal",
              ref="R7", value="100k")
    R8 = Part(f"{SYM}/Device.kicad_sym", "R",
              footprint="Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal",
              ref="R8", value="100k")
    R7[1] += gate_raw; R7[2] += gate_in
    R8[1] += gate_in;  R8[2] += gnd

    # ── Audio output (inverting summer) ────────────────────────────────────────

    R9 = Part(f"{SYM}/Device.kicad_sym", "R",
              footprint="Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal",
              ref="R9", value="100k")
    R10 = Part(f"{SYM}/Device.kicad_sym", "R",
               footprint="Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal",
               ref="R10", value="100k")
    R11 = Part(f"{SYM}/Device.kicad_sym", "R",
               footprint="Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal",
               ref="R11", value="100k")
    R9[1]  += aout_a; R9[2]  += inv_in
    R10[1] += aout_b; R10[2] += inv_in
    R11[1] += aout_c; R11[2] += inv_in

    # R12: 100kΩ feedback
    R12 = Part(f"{SYM}/Device.kicad_sym", "R",
               footprint="Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal",
               ref="R12", value="100k")
    R12[1] += inv_in; R12[2] += audio_sum

    # C11: 4.7nF LP filter (in parallel with R12)
    C11 = Part(f"{SYM}/Device.kicad_sym", "C",
               footprint="Capacitor_THT:C_Disc_D5.0mm_W2.5mm_P5.00mm",
               ref="C11", value="4.7nF")
    C11[1] += inv_in; C11[2] += audio_sum

    # C12: 1µF DC-blocking cap
    C12 = Part(f"{SYM}/Device.kicad_sym", "C_Polarized",
               footprint="Capacitor_THT:CP_Radial_D6.3mm_P2.50mm",
               ref="C12", value="1µF")
    C12[1] += audio_sum; C12[2] += audio_out

    # R13: 1kΩ output load to GND
    R13 = Part(f"{SYM}/Device.kicad_sym", "R",
               footprint="Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal",
               ref="R13", value="1k")
    R13[1] += audio_out; R13[2] += gnd

    # J3: audio output jack
    J3 = Part(f"{SYM}/Connector_Audio.kicad_sym", "AudioJack2",
              footprint="Connector_Audio:Jack_3.5mm_QingPu_WQP-PJ301BM_Vertical_CircularHoles",
              ref="J3", value="AUDIO_OUT")
    J3["S"] += gnd
    J3["T"] += audio_out


if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    ay_module()

    generate_netlist(file_="ay_module.net")
    print("Netlist written: ay_module.net")

    try:
        generate_schematic(file_="ay_module")
        print("Schematic written.")
    except Exception as e:
        print(f"Schematic note: {e}")
