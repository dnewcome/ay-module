# AY-3-8910 Eurorack Module — Design Plan

## Overview

Single-voice-controlled Eurorack module based on the AY-3-8910 PSG (40-pin DIP).
- 3 internal voices, controlled via MIDI (polyphonic) or CV/Gate (melody voice)
- Arduino Pro Micro (ATmega32U4) as controller
- Eurorack 3U format, targeting ~14HP

---

## Subsystems

### 1. Power
- **Connector**: Eurorack 16-pin IDC (±12V, +5V, GND)
- **+5V rail**: Derived from +12V via LM7805 (or MCP1700-5002 LDO) + 10µF/100nF decoupling
  - AY-3-8910 and Arduino both run on +5V
- **±12V**: Used only for op-amp audio stage (TL072 dual op-amp)
- **Reverse protection**: 1N4001 diode on +12V input

### 2. AY-3-8910 (U1, 40-pin DIP)
- **VCC** (pin 40): +5V, 100nF bypass cap to GND
- **GND** (pin 1): GND
- **Clock** (pin 22): 1MHz square wave from Arduino Timer1 (pin D9)
- **RESET** (pin 23): Active low, pulled high via 10kΩ, driven by Arduino D15
- **A8** (pin 25): tied to GND (256-word address space sufficient)
- **A9** (pin 24): tied to +5V (pulled up per datasheet recommendation)
- **TEST1** (pin 39), **TEST2** (pin 26): leave unconnected
- **Data bus DA0–DA7** (pins 37–30): Arduino D2, D3, D4, D5, D6, D7, D8, D10
- **BC1** (pin 29): tied to GND (simplified control scheme)
- **BDIR** (pin 27): Arduino D14 (A0)
- **BC2** (pin 28): Arduino D16 (A2)
- **IOB0–IOB7** (pins 13–6): unconnected (not used)
- **IOA0–IOA7** (pins 21–14): unconnected (not used)

**Simplified bus control (BC1=0):**
| BDIR | BC2 | Function  |
|------|-----|-----------|
| 0    | 0   | INACTIVE  |
| 1    | 0   | LATCH     |
| 1    | 1   | WRITE     |

### 3. Arduino Pro Micro (U2)
- **+5V**: from regulated rail, VCC pin
- **GND**: GND pin
- **D9**: Clock output to AY CLK (via 75Ω series resistor)
- **D15**: RESET output to AY RESET
- **D14 (A0)**: BDIR
- **D16 (A2)**: BC2
- **D2–D8, D10**: Data bus DA0–DA7
- **RX (D0/Serial1)**: MIDI RX (from optocoupler output)
- **A1**: CV input (0–5V after scaling)
- **A3**: Gate input (0–5V after clamping)
- **USB**: accessible via panel-mounted micro-USB passthrough (optional)

### 4. MIDI Input
- **Connector**: 5-pin DIN (panel mount)
- **Optocoupler**: 6N137
  - Pin 2 (anode) via 220Ω resistor to MIDI pin 4
  - Pin 3 (cathode) to MIDI pin 5
  - Pin 8 (VCC): +5V
  - Pin 5 (GND): GND
  - Pin 6 (Vo): pulled high via 10kΩ to +5V, output to Arduino RX (D0)
  - Pin 7 (enable): tied to +5V

### 5. CV Input (1V/oct)
- **Jack**: 3.5mm TRS (panel)
- Eurorack CV range: typically ±5V, 1V/oct
- **Scaling circuit** (TL072 op-amp, half):
  - Input: ±5V CV
  - Level shift + scale to 0–5V for Arduino ADC
  - Resistor network: R1=100kΩ (input), R2=100kΩ (to -12V ref divider)
  - Output clamped with 1N4148 diodes to 0V and +5V
  - 100nF filter cap on output
- Arduino A1 reads 0–5V → maps to MIDI note range

### 6. Gate Input
- **Jack**: 3.5mm TRS (panel)
- Eurorack gate: 0V / +5V (or +10V)
- Voltage divider: 100kΩ / 100kΩ → halves +10V max to 5V max
- Schottky diode (BAT42) clamp to +5V
- Arduino A3 (or digital pin with threshold) reads gate

### 7. Audio Output
- **Channels**: AoutA (pin 4), AoutB (pin 3), AoutC (pin 38) — all summed
- **Summing stage** (TL072 op-amp, other half):
  - 3 × 100kΩ input resistors summing into virtual ground of inverting amp
  - 100kΩ feedback resistor (unity sum gain)
  - Output: 4.7nF + 100kΩ RC lowpass filter
  - DC blocking: 1µF series cap to output jack
  - Output load resistor: 1kΩ to GND
- **Jack**: 3.5mm TRS (panel), mono

---

## Bill of Materials (initial)

| Ref  | Part               | Value/Part#         |
|------|--------------------|---------------------|
| U1   | AY-3-8910          | 40-pin DIP          |
| U2   | Arduino Pro Micro  | ATmega32U4, 5V/16MHz|
| U3   | Optocoupler        | 6N137               |
| U4   | Op-amp             | TL072               |
| U5   | Voltage regulator  | LM7805 or MCP1700-5 |
| C1   | Bypass cap         | 100nF               |
| C2   | Bypass cap         | 100nF               |
| C3   | DC blocking cap    | 1µF electrolytic    |
| C4   | Audio filter cap   | 4.7nF               |
| C5,C6| Reg filter caps    | 10µF electrolytic   |
| D1   | Reverse protect    | 1N4001              |
| D2   | MIDI diode         | 1N4148              |
| D3,D4| CV clamp           | BAT42 Schottky      |
| R1   | MIDI current limit | 220Ω                |
| R2   | MIDI pull-up       | 10kΩ                |
| R3   | RESET pull-up      | 10kΩ                |
| R4   | CLK series         | 75Ω                 |
| R5–R7| Audio sum inputs   | 100kΩ × 3           |
| R8   | Audio feedback     | 100kΩ               |
| R9   | Audio output load  | 1kΩ                 |
| R10  | Audio LP filter    | 100kΩ               |
| R11,R12| CV scaling     | 100kΩ × 2           |
| R13,R14| Gate divider   | 100kΩ × 2           |
| J1   | Eurorack power     | 16-pin IDC          |
| J2   | MIDI in            | 5-pin DIN           |
| J3   | Audio out          | 3.5mm TRS           |
| J4   | CV in              | 3.5mm TRS           |
| J5   | Gate in            | 3.5mm TRS           |

---

## Next Steps

1. Create KiCad schematic (.kicad_sch) with all subsystems
2. Assign footprints (DIP-40, DIP-8, DIP-14, TO-220, 3.5mm jacks, IDC)
3. Run ERC in KiCad
4. Panel layout (14HP, 3U)
5. PCB layout with power plane

---

## Open Questions

- Arduino mounted directly on PCB (through-hole headers) or via USB connector to panel?
- Single or double-sided PCB?
- Panel-mount MIDI DIN or PCB-mount?
