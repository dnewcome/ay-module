# AY-3-8910 Eurorack Module

A Eurorack synthesizer module built around the General Instrument AY-3-8910 programmable sound generator (PSG). The module provides 3 voices controlled via MIDI or CV/Gate, housed in a ~14HP 3U Eurorack panel.

## Project Goal

Build a working KiCad schematic and PCB for a Eurorack-compatible AY-3-8910 module with:

- **Single AY-3-8910** (40-pin DIP) — 3 simultaneous oscillator voices
- **MIDI input** — 3.5mm TRS Type A with optoisolator, all channels, polyphonic
- **CV/Gate input** — 1V/oct bipolar CV (±10V), 5V gate with input protection
- **Mono audio output** — summed voices, line level, DC-blocked
- **Arduino Pro Micro** (ATmega32U4, 5V/16MHz) as controller
- **Eurorack power** — ±12V backplane, onboard 5V regulation, no USB power in rack, no backfeed

## Reference Design

Based on the [Dual AY-3-8910 MIDI module by Doge Microsystems](https://www.instructables.com/Arduino-MIDI-Chiptune-Synthesizer/), which is itself derived from TheSpodShed's Arduino MIDI chiptune synthesizer on Instructables.

The reference design uses a simplified bus control scheme (BC1 grounded, only BDIR/BC2 toggled) to avoid timing-sensitive transitions:

| BDIR | BC2 | BC1 | Function |
|------|-----|-----|----------|
| 0    | 0   | 0   | INACTIVE |
| 1    | 0   | 0   | LATCH    |
| 1    | 1   | 0   | WRITE    |

Key difference from this project: the reference runs two AY chips off USB power. This module targets a single chip, Eurorack power, and adds Eurorack-standard CV/Gate inputs.

## Repository Contents

| File/Dir | Description |
|----------|-------------|
| `PLAN.md` | Detailed subsystem design plan (pinout, BOM, signal routing) |
| `design.md` | Full reference design documentation including Arduino firmware |
| `ay_skidl.py` | SKiDL-based schematic generation script (main attempt) |
| `ay_skidl_sklib.py` | SKiDL custom symbol library definitions |
| `circuit_ay_arduino_cv_audio.py` | SKiDL circuit: AY chip + Arduino + CV + audio |
| `circuit_power_midi.py` | SKiDL circuit: power supply + MIDI input |
| `generate_schematic.py` | Top-level schematic generation entry point |
| `ay-module.kicad_sch` | KiCad schematic (manual/partial) |
| `ay_module.kicad_sch` | KiCad schematic (SKiDL-generated) |
| `ay-module.kicad_sym` | Custom KiCad symbol library |
| `ay_module.net` | Netlist output from SKiDL |
| `lib_symbols.py` | Symbol/footprint library helpers |
| `celus/` | Celus AI design session notes and exported files |
| `ay-module-backups/` | KiCad project backups |
| `generalinstrument_ay-3-8910.pdf` | AY-3-8910 datasheet |
| `Dual_AY-3-8910_circuit.png` | Reference circuit diagram |
| `AY-3-8910_control.png` | AY bus control timing reference |
| `ay-module-schematic.png` / `ay-module-detailed.png` | Schematic screenshots |

## Approach: AI-Assisted Circuit Design

This repo is an experiment in using AI tools to generate a complete KiCad schematic from a specification. Two approaches have been tried:

### SKiDL (Python netlist generation)
Using [SKiDL](https://devbisme.github.io/skidl/) — a Python DSL for describing circuits as code — with Claude generating the Python scripts. The goal is to produce a `.net` netlist that can be imported into KiCad for layout.

Status: Scripts run and produce a netlist (`ay_module.net`), but the resulting schematic has had correctness issues.

### Celus
Using [Celus](https://www.celus.io/) — an AI-native EDA tool — via its design canvas workflow. The Celus session captured the full design intent (see `celus/celus.md`) and produced a functional block architecture, pending CUBO resolve and KiCad export.

Status: Functional block design created; CUBO resolve and export not yet completed.

## Design Summary

See `PLAN.md` for the full subsystem breakdown. Key points:

- **Power**: +12V → LM7805 → +5V for AY + Arduino; ±12V for op-amp audio stage
- **AY clock**: 1MHz square wave from Arduino Timer1 (pin D9)
- **Audio output**: 3-resistor summing amp (TL072), RC lowpass, 1µF DC blocking cap
- **CV input**: ±10V → op-amp level shift to 0–5V → Arduino ADC, Schottky diode clamps
- **MIDI**: 3.5mm TRS Type A → 6N137 optoisolator → Arduino Serial1 RX

## Status

Work in progress. The schematic has not been verified as correct or complete. No PCB layout exists yet.

**Known open issues:**
- SKiDL-generated schematic needs ERC verification in KiCad
- Celus export to KiCad not yet done
- Arduino mounting strategy (on-PCB vs panel USB) not finalized
- Panel layout (14HP) not started
