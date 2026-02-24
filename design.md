<span id="top"></span>

# Dual AY-3-8910 MIDI module

From Doge Microsystems

<a href="#mw-head" class="mw-jump-link">Jump to navigation</a>
<a href="#p-search" class="mw-jump-link">Jump to search</a>

For the last couple years I've been fascinated by
<a href="https://en.wikipedia.org/wiki/MIDI" class="external text"
rel="nofollow">MIDI</a> and its ability to both play music in real time
and record the signalling for later playback and refinement. That's all
well and good but wheres the fun in just buying off the shelf equipment
when you could make your own? Specifically I'm talking about MIDI
controlled "sound modules" that take a MIDI input, and output sound.
Often you would use MIDI to control a synthesizer, electric piano, or
some other purpose built instrument; but why not
<a href="https://en.wikipedia.org/wiki/Programmable_sound_generator"
class="external text" rel="nofollow">programmable sound generators</a>
(PSG) like an
<a href="https://en.wikipedia.org/wiki/General_Instrument_AY-3-8910"
class="external text" rel="nofollow">AY-3-8910</a> from General
Instruments!

There are several guides and hundreds of other people that have done
this previously with a single chip but I want to control two chips at
once. A single 8910 has 3 output channels, so it can play 3 notes at
once. With a bit of work, and the correct timing, multiple chips can be
used together to increase the simultaneous note count.

  
My work below is a derivative of the code and design by TheSpodShed on
Instructables available here: <a
href="https://www.instructables.com/Arduino-MIDI-Chiptune-Synthesizer/"
class="external free"
rel="nofollow">https://www.instructables.com/Arduino-MIDI-Chiptune-Synthesizer/</a>

## Contents

<span class="toctogglespan"></span>

-   [<span class="tocnumber">1</span>
    <span class="toctext">Theory</span>](#Theory)
-   [<span class="tocnumber">2</span> <span class="toctext">The
    circuit</span>](#The_circuit)
-   [<span class="tocnumber">3</span>
    <span class="toctext">Code</span>](#Code)

## <span id="Theory" class="mw-headline">Theory</span>

The AY-3-9810 is relatively simple to work with requiring only a data
bus, a couple control lines, a 1 MHz clock, and reset. The datasheet (<a
href="http://map.grauw.nl/resources/sound/generalinstrument_ay-3-8910.pdf"
class="external text" rel="nofollow">available here</a>) describes the
connectivity requirements in detail. The code by TheSpodShed has a neat
feature where if more than 3 notes are played at once one of the middle
notes will be dropped while the highest and lowest notes continue to
play. This does a pretty good job of getting around the note limitation
but it isn't without its faults.

To control two chips the data bus, clock, and reset can be shared but we
need two more I/O pins on the Arduino (more on this later).

## <span id="The_circuit" class="mw-headline">The circuit</span>

<a href="/wiki/File:Dual_AY-3-8910_circuit.png" class="image"><img
src="/mywiki/images/e/e6/Dual_AY-3-8910_circuit.png" width="980"
height="760" alt="Dual AY-3-8910 circuit.png" /></a>

The entire circuit is powered by over USB and the Arduino generates the
1 MHz clock for simplicity's sake.

<a href="/wiki/File:AY-3-8910_control.png" class="image"><img
src="/mywiki/images/thumb/6/69/AY-3-8910_control.png/450px-AY-3-8910_control.png"
class="thumbimage"
srcset="/mywiki/images/6/69/AY-3-8910_control.png 1.5x" width="450"
height="583" alt="AY-3-8910 control.png" /></a>

<a href="/wiki/File:AY-3-8910_control.png" class="internal"
title="Enlarge"></a>

The AY-3-8910 datasheet provides a reduced control scheme to save an I/O
pin but I was unable to get this work reliably. I instead came up with
an *alternative* reduced control scheme.

The original control scheme can be reduced to a much simpler to use
method where BC1 is grounded and READ is never used. This allows the
Arduino to change one output at a time to transition between states
removing the need for precise timing.

<table class="wikitable">
<tbody>
<tr class="header">
<th>BDIR</th>
<th>BC2</th>
<th>BC1</th>
<th>Function</th>
</tr>
&#10;<tr class="odd">
<td>0</td>
<td>0</td>
<td>0</td>
<td>INACTIVE</td>
</tr>
<tr class="even">
<td>1</td>
<td>1</td>
<td>0</td>
<td>WRITE</td>
</tr>
<tr class="odd">
<td>1</td>
<td>0</td>
<td>0</td>
<td>LATCH</td>
</tr>
</tbody>
</table>

## <span id="Code" class="mw-headline">Code</span>

You will need the Arduino MIDI library installed as well as the USBMIDI
library if you want to use USB.

Download here: [File:Dual AY-3-8910
MIDI.ino](/wiki/File:Dual_AY-3-8910_MIDI.ino "File:Dual AY-3-8910 MIDI.ino")

      1 // Uncomment to enable traiditonal serial midi
      2 #define SERIALMIDI
      3 
      4 // Uncomment to enable USB midi
      5 #define USBMIDI
      6 
      7 // Uncomment to enable debugging output over USB serial
      8 //#define DEBUG
      9 
     10 #include <avr/io.h>
     11 
     12 #ifdef USBMIDI
     13 #include "MIDIUSB.h"
     14 #endif
     15 
     16 // We borrow one struct from MIDIUSB for traditional serial midi, so define it if were not using USBMIDI
     17 #ifndef MIDIUSB_h
     18 typedef struct
     19 {
     20   uint8_t header;
     21   uint8_t byte1;
     22   uint8_t byte2;
     23   uint8_t byte3;
     24 } midiEventPacket_t;
     25 #endif
     26 
     27 #ifdef SERIALMIDI
     28 #include <MIDI.h>
     29 MIDI_CREATE_INSTANCE(HardwareSerial, Serial1, MIDI);//Serial1 on pro micro
     30 #endif
     31 
     32 typedef unsigned short int ushort;
     33 
     34 typedef unsigned char note_t;
     35 #define NOTE_OFF 0
     36 
     37 typedef unsigned char midictrl_t;
     38 
     39 // Pin driver ---------------------------------------------
     40 
     41 static const int dbus[8] = { 2, 3, 4, 5, 6, 7, 8, 10 };
     42 
     43 static const ushort
     44   BC2_A = 16,
     45   BDIR_A = 14,
     46   BC2_B = A0,
     47   BDIR_B = A1,
     48   nRESET = 15,
     49   clkOUT = 9;
     50 
     51 static const ushort DIVISOR = 7; // Set for 1MHz clock
     52 
     53 static void clockSetup() {
     54    // Timer 1 setup for Mega32U4 devices
     55    //
     56    // Use CTC mode: WGM13..0 = 0100
     57    // Toggle OC1A on Compare Match: COM1A1..0 = 01
     58    // Use ClkIO with no prescaling: CS12..0 = 001
     59    // Interrupts off: TIMSK0 = 0
     60    // OCR0A = interval value
     61    
     62    TCCR1A = (1 << COM1A0);
     63    TCCR1B = (1 << WGM12) | (1 << CS10);
     64    TCCR1C = 0;
     65    TIMSK1 = 0;
     66    OCR1AH = 0;
     67    OCR1AL = DIVISOR; // NB write high byte first
     68 }
     69 
     70 static void setData(unsigned char db) {
     71   unsigned char bit = 1;
     72   for (ushort i = 0; i < 8; i++) {
     73     digitalWrite(dbus[i], (db & bit) ? HIGH : LOW);
     74     bit <<= 1;
     75   }
     76 }
     77 
     78 static void writeReg_A(unsigned char reg, unsigned char db) {
     79   // This is a bit of an odd way to do it, BC1 is kept low and NACT, BAR, IAB, and DWS are used.
     80   // BC1 is kept low the entire time.
     81   
     82   // Inactive (BDIR BC2 BC1 0 0 0)
     83   digitalWrite(BDIR_A, LOW);
     84   digitalWrite(BC2_A, LOW);
     85 
     86   //Set register address
     87   setData(reg);
     88 
     89   // BAR (Latch) (BDIR BC2 BC1 1 0 0)
     90   digitalWrite(BDIR_A, HIGH);
     91 
     92   // Inactive (BDIR BC2 BC1 0 0 0)
     93   digitalWrite(BDIR_A, LOW);
     94   
     95   //Set register contents
     96   setData(db);
     97 
     98   // Write (BDIR BC2 BC1 1 1 0)
     99   digitalWrite(BC2_A, HIGH);
    100   digitalWrite(BDIR_A, HIGH);
    101 
    102   // Inactive (BDIR BC2 BC1 0 0 0)
    103   digitalWrite(BC2_A, LOW);
    104   digitalWrite(BDIR_A, LOW);
    105 }
    106 
    107 static void writeReg_B(unsigned char reg, unsigned char db) {
    108   // This is a bit of an odd way to do it, BC1 is kept low and NACT, BAR, IAB, and DWS are used.
    109   // BC1 is kept low the entire time.
    110   
    111   // Inactive (BDIR BC2 BC1 0 0 0)
    112   digitalWrite(BDIR_B, LOW);
    113   digitalWrite(BC2_B, LOW);
    114 
    115   //Set register address
    116   setData(reg);
    117 
    118   // BAR (Latch) (BDIR BC2 BC1 1 0 0)
    119   digitalWrite(BDIR_B, HIGH);
    120 
    121   // Inactive (BDIR BC2 BC1 0 0 0)
    122   digitalWrite(BDIR_B, LOW);
    123   
    124   //Set register contents
    125   setData(db);
    126 
    127   // Write (BDIR BC2 BC1 1 1 0)
    128   digitalWrite(BC2_B, HIGH);
    129   digitalWrite(BDIR_B, HIGH);
    130 
    131   // Inactive (BDIR BC2 BC1 0 0 0)
    132   digitalWrite(BC2_B, LOW);
    133   digitalWrite(BDIR_B, LOW);
    134 }
    135 
    136 // AY-3-8910 driver ---------------------------------------
    137 
    138 class PSGRegs {
    139 public:
    140   enum {
    141     TONEALOW = 0,
    142     TONEAHIGH,
    143     TONEBLOW,
    144     TONEBHIGH,
    145     TONECLOW,
    146     TONECHIGH,
    147     NOISEGEN,
    148     MIXER,
    149     
    150     TONEAAMPL,
    151     TONEBAMPL,
    152     TONECAMPL,
    153     ENVLOW,
    154     ENVHIGH,
    155     ENVSHAPE,
    156     IOA,
    157     IOB
    158   };
    159   
    160   unsigned char regs_A[16];
    161   unsigned char regs_B[16];
    162 
    163   unsigned char lastregs_A[16];
    164   unsigned char lastregs_B[16];
    165 
    166   void init() {
    167     for (int i = 0; i < 16; i++) {
    168       regs_A[i] = lastregs_A[i] = 0xFF;
    169       writeReg_A(i, regs_A[i]);
    170 
    171       regs_B[i] = lastregs_B[i] = 0xFF;
    172       writeReg_B(i, regs_B[i]);
    173     }
    174   }
    175   
    176   void update() {
    177     for (int i = 0; i < 16; i++) {
    178       if (regs_A[i] != lastregs_A[i]) {
    179         writeReg_A(i, regs_A[i]);
    180         lastregs_A[i] = regs_A[i];
    181       }
    182 
    183       if (regs_B[i] != lastregs_B[i]) {
    184         writeReg_B(i, regs_B[i]);
    185         lastregs_B[i] = regs_B[i];
    186       }
    187     }
    188   }
    189 
    190   void setTone(ushort ch, ushort divisor, ushort ampl) {
    191     if (ch > 2) {
    192       //reduce channel to usable range
    193       ch = ch - 3;
    194       //use regs_B
    195       regs_B[TONEALOW  + (ch<<1)] = (divisor & 0xFF);
    196       regs_B[TONEAHIGH + (ch<<1)] = (divisor >> 8);
    197       regs_B[TONEAAMPL + ch] = ampl;
    198       
    199       ushort mask = (8+1) << ch;
    200       regs_B[MIXER] = (regs_B[MIXER] | mask) ^ (1 << ch);
    201 
    202       return;
    203     }
    204     
    205     regs_A[TONEALOW  + (ch<<1)] = (divisor & 0xFF);
    206     regs_A[TONEAHIGH + (ch<<1)] = (divisor >> 8);
    207     regs_A[TONEAAMPL + ch] = ampl;
    208     
    209     ushort mask = (8+1) << ch;
    210     regs_A[MIXER] = (regs_A[MIXER] | mask) ^ (1 << ch);
    211   }
    212 
    213   void setToneAndNoise(ushort ch, ushort divisor, ushort noisefreq, ushort ampl) {
    214     if (ch > 2) {
    215       //reduce channel to usable range
    216       ch = ch - 3;
    217       //use regs_B
    218       regs_B[TONEALOW  + (ch<<1)] = (divisor & 0xFF);
    219       regs_B[TONEAHIGH + (ch<<1)] = (divisor >> 8);
    220       regs_B[NOISEGEN] = noisefreq;
    221       regs_B[TONEAAMPL + ch] = ampl;
    222       
    223       ushort mask = (8+1) << ch;
    224       ushort bits = (noisefreq < 16 ? 8 : 0) + (divisor > 0 ? 1 : 0);
    225       regs_B[MIXER] = (regs_B[MIXER] | mask) ^ (bits << ch);
    226 
    227       return;
    228     }
    229     
    230     regs_A[TONEALOW  + (ch<<1)] = (divisor & 0xFF);
    231     regs_A[TONEAHIGH + (ch<<1)] = (divisor >> 8);
    232     regs_A[NOISEGEN] = noisefreq;
    233     regs_A[TONEAAMPL + ch] = ampl;
    234     
    235     ushort mask = (8+1) << ch;
    236     ushort bits = (noisefreq < 16 ? 8 : 0) + (divisor > 0 ? 1 : 0);
    237     regs_A[MIXER] = (regs_A[MIXER] | mask) ^ (bits << ch);
    238   }
    239 
    240   void setEnvelope(ushort divisor, ushort shape) {
    241     regs_A[ENVLOW]  = (divisor & 0xFF);
    242     regs_A[ENVHIGH] = (divisor >> 8);
    243     regs_A[ENVSHAPE] = shape;
    244 
    245     regs_B[ENVLOW]  = (divisor & 0xFF);
    246     regs_B[ENVHIGH] = (divisor >> 8);
    247     regs_B[ENVSHAPE] = shape; 
    248   }
    249   
    250   void setOff(ushort ch) {
    251     if (ch > 2) {
    252       //reduce channel to usable range
    253       ch = ch - 3;
    254       //use regs_B
    255       ushort mask = (8+1) << ch;
    256       regs_B[MIXER] = (regs_A[MIXER] | mask);
    257       regs_B[TONEAAMPL + ch] = 0;
    258       if (regs_B[ENVSHAPE] != 0) {
    259         regs_B[ENVSHAPE] = 0;
    260         update(); // Force flush
    261       }
    262 
    263       return;
    264     }
    265     
    266     ushort mask = (8+1) << ch;
    267     regs_A[MIXER] = (regs_A[MIXER] | mask);
    268     regs_A[TONEAAMPL + ch] = 0;
    269     if (regs_A[ENVSHAPE] != 0) {
    270       regs_A[ENVSHAPE] = 0;
    271       update(); // Force flush
    272     }
    273   }
    274 };
    275 
    276 static PSGRegs psg;
    277 
    278 // Voice generation ---------------------------------------
    279 
    280 static const ushort
    281   MIDI_MIN = 24,
    282   MIDI_MAX = 96,
    283   N_NOTES = (MIDI_MAX+1-MIDI_MIN);
    284 
    285 static const ushort note_table[N_NOTES] = {
    286    1911, // MIDI 24, 32.70 Hz
    287    1804, // MIDI 25, 34.65 Hz
    288    1703, // MIDI 26, 36.71 Hz
    289    1607, // MIDI 27, 38.89 Hz
    290    1517, // MIDI 28, 41.20 Hz
    291    1432, // MIDI 29, 43.65 Hz
    292    1351, // MIDI 30, 46.25 Hz
    293    1276, // MIDI 31, 49.00 Hz
    294    1204, // MIDI 32, 51.91 Hz
    295    1136, // MIDI 33, 55.00 Hz
    296    1073, // MIDI 34, 58.27 Hz
    297    1012, // MIDI 35, 61.74 Hz
    298    956, // MIDI 36, 65.41 Hz
    299    902, // MIDI 37, 69.30 Hz
    300    851, // MIDI 38, 73.42 Hz
    301    804, // MIDI 39, 77.78 Hz
    302    758, // MIDI 40, 82.41 Hz
    303    716, // MIDI 41, 87.31 Hz
    304    676, // MIDI 42, 92.50 Hz
    305    638, // MIDI 43, 98.00 Hz
    306    602, // MIDI 44, 103.83 Hz
    307    568, // MIDI 45, 110.00 Hz
    308    536, // MIDI 46, 116.54 Hz
    309    506, // MIDI 47, 123.47 Hz
    310    478, // MIDI 48, 130.81 Hz
    311    451, // MIDI 49, 138.59 Hz
    312    426, // MIDI 50, 146.83 Hz
    313    402, // MIDI 51, 155.56 Hz
    314    379, // MIDI 52, 164.81 Hz
    315    358, // MIDI 53, 174.61 Hz
    316    338, // MIDI 54, 185.00 Hz
    317    319, // MIDI 55, 196.00 Hz
    318    301, // MIDI 56, 207.65 Hz
    319    284, // MIDI 57, 220.00 Hz
    320    268, // MIDI 58, 233.08 Hz
    321    253, // MIDI 59, 246.94 Hz
    322    239, // MIDI 60, 261.63 Hz
    323    225, // MIDI 61, 277.18 Hz
    324    213, // MIDI 62, 293.66 Hz
    325    201, // MIDI 63, 311.13 Hz
    326    190, // MIDI 64, 329.63 Hz
    327    179, // MIDI 65, 349.23 Hz
    328    169, // MIDI 66, 369.99 Hz
    329    159, // MIDI 67, 392.00 Hz
    330    150, // MIDI 68, 415.30 Hz
    331    142, // MIDI 69, 440.00 Hz
    332    134, // MIDI 70, 466.16 Hz
    333    127, // MIDI 71, 493.88 Hz
    334    119, // MIDI 72, 523.25 Hz
    335    113, // MIDI 73, 554.37 Hz
    336    106, // MIDI 74, 587.33 Hz
    337    100, // MIDI 75, 622.25 Hz
    338    95, // MIDI 76, 659.26 Hz
    339    89, // MIDI 77, 698.46 Hz
    340    84, // MIDI 78, 739.99 Hz
    341    80, // MIDI 79, 783.99 Hz
    342    75, // MIDI 80, 830.61 Hz
    343    71, // MIDI 81, 880.00 Hz
    344    67, // MIDI 82, 932.33 Hz
    345    63, // MIDI 83, 987.77 Hz
    346    60, // MIDI 84, 1046.50 Hz
    347    56, // MIDI 85, 1108.73 Hz
    348    53, // MIDI 86, 1174.66 Hz
    349    50, // MIDI 87, 1244.51 Hz
    350    47, // MIDI 88, 1318.51 Hz
    351    45, // MIDI 89, 1396.91 Hz
    352    42, // MIDI 90, 1479.98 Hz
    353    40, // MIDI 91, 1567.98 Hz
    354    38, // MIDI 92, 1661.22 Hz
    355    36, // MIDI 93, 1760.00 Hz
    356    34, // MIDI 94, 1864.66 Hz
    357    32, // MIDI 95, 1975.53 Hz
    358    30, // MIDI 96, 2093.00 Hz
    359 };
    360 
    361 struct FXParams {
    362   ushort noisefreq;
    363   ushort tonefreq;
    364   ushort envdecay;
    365   ushort freqdecay;
    366   ushort timer;
    367 };
    368 
    369 struct ToneParams {
    370   ushort decay;
    371   ushort sustain; // Values 0..32
    372   ushort release;
    373 };
    374 
    375 static const ushort MAX_TONES = 4;
    376 static const ToneParams tones[MAX_TONES] = {
    377   { 30, 24, 10 },
    378   { 30, 12, 8 },
    379   { 5,  8,  7 },
    380   { 10, 31, 30 }
    381 };
    382 
    383 class Voice {
    384 public:
    385   ushort m_chan;  // Index to psg channel 
    386   ushort m_pitch;
    387   int m_ampl, m_decay, m_sustain, m_release;
    388   static const int AMPL_MAX = 1023;
    389   ushort m_adsr;
    390 
    391   void init (ushort chan) {
    392     m_chan = chan;
    393     m_ampl = m_sustain = 0;
    394     kill();
    395   }
    396   
    397   void start(note_t note, midictrl_t vel, midictrl_t chan) {
    398     const ToneParams *tp = &tones[chan % MAX_TONES];
    399     
    400     m_pitch = note_table[note - MIDI_MIN];
    401     if (vel > 127) {
    402       m_ampl = AMPL_MAX;
    403     }
    404     else {
    405       m_ampl = 768 + (vel << 1);
    406     }
    407     m_decay = tp->decay;
    408     m_sustain = (m_ampl * tp->sustain) >> 5;
    409     m_release = tp->release;
    410     m_adsr = 'D';
    411     psg.setTone(m_chan, m_pitch, m_ampl >> 6);
    412   }
    413 
    414   struct FXParams m_fxp;
    415   
    416   void startFX(const struct FXParams &fxp) {
    417     m_fxp = fxp;
    418   
    419     if (m_ampl > 0) {
    420       psg.setOff(m_chan);
    421     }
    422     m_ampl = AMPL_MAX;
    423     m_adsr = 'X';
    424     m_decay = fxp.timer;
    425 
    426     psg.setEnvelope(fxp.envdecay, 9); 
    427     psg.setToneAndNoise(m_chan, fxp.tonefreq, fxp.noisefreq, 31);
    428   }
    429   
    430 
    431   void stop() {
    432     if (m_adsr == 'X') {
    433       return; // Will finish when ready...
    434     }
    435       
    436     if (m_ampl > 0) {
    437       m_adsr = 'R';
    438     }
    439     else {
    440       psg.setOff(m_chan);
    441     }
    442   }
    443   
    444   void update100Hz() {
    445     if (m_ampl == 0) {
    446       return;
    447     }
    448       
    449     switch(m_adsr) {
    450       case 'D':
    451         m_ampl -= m_decay;
    452         if (m_ampl <= m_sustain) {
    453           m_adsr = 'S';
    454           m_ampl = m_sustain;
    455         }
    456         break;
    457 
    458       case 'S':
    459         break;
    460 
    461       case 'R':
    462         if ( m_ampl < m_release ) {
    463           m_ampl = 0;
    464         }
    465         else {
    466           m_ampl -= m_release;
    467         }
    468         break;
    469 
    470       case 'X':
    471         // FX is playing.         
    472         if (m_fxp.freqdecay > 0) { 
    473           m_fxp.tonefreq += m_fxp.freqdecay;
    474           psg.setToneAndNoise(m_chan, m_fxp.tonefreq, m_fxp.noisefreq, 31);
    475         }
    476         
    477         m_ampl -= m_decay;
    478         if (m_ampl <= 0) {
    479           psg.setOff(m_chan);
    480           m_ampl = 0;
    481         }
    482         return;
    483         
    484       default:
    485         break;
    486     }  
    487 
    488     if (m_ampl > 0) {
    489       psg.setTone(m_chan, m_pitch, m_ampl >> 6);
    490     }
    491     else {
    492       psg.setOff(m_chan);    
    493     }
    494   }
    495   
    496   bool isPlaying() {
    497     return (m_ampl > 0);
    498   }
    499   
    500   void kill() {
    501     psg.setOff(m_chan);
    502     m_ampl = 0;
    503   }
    504 };
    505 
    506 
    507 const ushort MAX_VOICES = 6;
    508 
    509 static Voice voices[MAX_VOICES];
    510 
    511 // MIDI synthesiser ---------------------------------------
    512 
    513 // Deals with assigning note on/note off to voices
    514 
    515 static const uint8_t PERC_CHANNEL = 9;
    516 
    517 static const note_t
    518   PERC_MIN = 35,
    519   PERC_MAX = 50;
    520   
    521 static const struct FXParams perc_params[PERC_MAX-PERC_MIN+1] = {
    522   // Mappings are from the General MIDI spec at https://www.midi.org/specifications-old/item/gm-level-1-sound-set
    523   
    524   // Params are: noisefreq, tonefreq, envdecay, freqdecay, timer
    525   
    526   { 9, 900, 800, 40, 50 },   // 35 Acoustic bass drum
    527   { 8, 1000, 700, 40, 50 },  // 36 (C) Bass Drum 1
    528   { 4, 0, 300, 0, 80 },      // 37 Side Stick
    529   { 6, 0, 1200, 0, 30  },    // 38 Acoustic snare
    530   
    531   { 5, 0, 1500, 0, 90 },     // 39 (D#) Hand clap
    532   { 6, 400, 1200, 11, 30  }, // 40 Electric snare
    533   { 16, 700, 800, 20, 30 },  // 41 Low floor tom
    534   { 0, 0, 300, 0, 80 },      // 42 Closed Hi Hat
    535   
    536   { 16, 400, 800, 13, 30 },   // 43 (G) High Floor Tom
    537   { 0, 0, 600, 0, 50 },      // 44 Pedal Hi-Hat
    538   { 16, 800, 1400, 30, 25 }, // 45 Low Tom
    539   { 0, 0, 800, 0, 40 },      // 46 Open Hi-Hat
    540   
    541   { 16, 600, 1400, 20, 25 }, // 47 (B) Low-Mid Tom
    542   { 16, 450, 1500, 15, 22 }, // 48 Hi-Mid Tom
    543   { 1, 0, 1800, 0, 25 },     // 49 Crash Cymbal 1
    544   { 16, 300, 1500, 10, 22 }, // 50 High Tom
    545 };
    546   
    547   
    548 
    549 static const int REQ_MAP_SIZE = (N_NOTES+7) / 8;
    550 static uint8_t m_requestMap[REQ_MAP_SIZE];
    551   // Bit is set for each note being requested
    552 static  midictrl_t m_velocity[N_NOTES];
    553   // Requested velocity for each note
    554 static  midictrl_t m_chan[N_NOTES];
    555   // Requested MIDI channel for each note
    556 static uint8_t m_highest, m_lowest;
    557   // Highest and lowest requested notes
    558 
    559 static const uint8_t NO_NOTE = 0xFF;
    560 static const uint8_t PERC_NOTE = 0xFE;
    561 static uint8_t m_playing[MAX_VOICES];
    562   // Which note each voice is playing
    563 
    564 static const uint8_t NO_VOICE = 0xFF;
    565 static uint8_t m_voiceNo[N_NOTES];
    566   // Which voice is playing each note
    567   
    568 
    569 static bool startNote(ushort idx) {
    570   for (ushort i = 0; i < MAX_VOICES; i++) {
    571     if (m_playing[i] == NO_NOTE) {
    572       voices[i].start(MIDI_MIN + idx, m_velocity[idx], m_chan[idx]);
    573       m_playing[i] = idx;
    574       m_voiceNo[idx] = i;
    575       return true;
    576     }
    577   }
    578   return false;
    579 }
    580   
    581 static bool startPercussion(note_t note) {
    582   ushort i;
    583   for (i = 0; i < MAX_VOICES; i++) {
    584     if (m_playing[i] == NO_NOTE || m_playing[i] == PERC_NOTE) {
    585       if (note >= PERC_MIN && note <= PERC_MAX) {
    586         voices[i].startFX(perc_params[note-PERC_MIN]);
    587         m_playing[i] = PERC_NOTE;
    588       }
    589       return true;
    590     }        
    591   }
    592   return false;
    593 }
    594     
    595 static bool stopNote(ushort idx) {
    596   uint8_t v = m_voiceNo[idx];
    597   if (v != NO_VOICE) {
    598     voices[v].stop();
    599     m_playing[v] = NO_NOTE;
    600     m_voiceNo[idx] = NO_VOICE;
    601     return true;
    602   }
    603   return false;
    604 }
    605 
    606 static void stopOneNote() {
    607   uint8_t v, chosen = NO_NOTE;
    608 
    609   // At this point we have run out of voices.
    610   // Pick a voice and stop it. We leave a voice alone
    611   // if it's playing the highest requested note. If it's
    612   // playing the lowest requested note we look for a 'better'
    613   // note, but stop it if none found.
    614 
    615   for (v = 0; v < MAX_VOICES; v++) {
    616     uint8_t idx = m_playing[v];
    617     if (idx == NO_NOTE) {// Uh? Perhaps called by mistake.
    618       return;
    619     }
    620 
    621     if (idx == m_highest) {
    622       continue;
    623     }
    624 
    625     if (idx == PERC_NOTE) {
    626       continue;
    627     }
    628       
    629     chosen = idx;
    630     if (idx != m_lowest) {
    631       break;
    632     }
    633     // else keep going, we may find a better one
    634   }
    635 
    636   if (chosen != NO_NOTE) {
    637     stopNote(chosen);
    638   }
    639 }
    640 
    641 static void updateRequestedNotes() {
    642   m_highest = m_lowest = NO_NOTE;
    643   ushort i,j;
    644     
    645   // Check highest requested note is playing
    646   // Return true if note was restarted; false if already playing 
    647   for (i = 0; i < REQ_MAP_SIZE; i++) {
    648     uint8_t req = m_requestMap[i];
    649     if (req == 0) {
    650       continue;
    651     }
    652 
    653     for (j = 0; j < 8; j++) {
    654       if (req & (1 << j)) {
    655         ushort idx = i*8 + j;
    656         if (m_lowest == NO_NOTE || m_lowest > idx) {
    657           m_lowest = idx;
    658         }
    659         if (m_highest==NO_NOTE || m_highest < idx)  {
    660           m_highest = idx;
    661         }
    662       }
    663     }
    664   }
    665 }
    666 
    667 static bool restartANote() {
    668   if (m_highest != NO_NOTE && m_voiceNo[m_highest] == NO_VOICE) {
    669     return startNote(m_highest);
    670   }
    671 
    672   if (m_lowest != NO_NOTE && m_voiceNo[m_lowest] == NO_VOICE) {
    673     return startNote(m_lowest);
    674   }
    675 
    676   return false;
    677 }
    678   
    679 static void synth_init () {
    680   ushort i;
    681 
    682   for (i = 0; i < REQ_MAP_SIZE; i++) {
    683     m_requestMap[i] = 0;
    684   }
    685 
    686   for (i = 0; i < N_NOTES; i++) {
    687     m_velocity[i] = 0;
    688     m_voiceNo[i] = NO_VOICE;
    689   }
    690     
    691   for (i = 0; i < MAX_VOICES; i++) {
    692     m_playing[i] = NO_NOTE;
    693   }
    694     
    695   m_highest = m_lowest = NO_NOTE;
    696 }
    697 
    698 static void noteOff(midictrl_t chan, note_t note, midictrl_t vel) {
    699   if (chan == PERC_CHANNEL || note < MIDI_MIN || note > MIDI_MAX) {
    700     return; // Just ignore it
    701   }
    702 
    703   ushort idx = note - MIDI_MIN;
    704 
    705   m_requestMap[idx/8] &= ~(1 << (idx & 7));
    706   m_velocity[idx] = 0;
    707   updateRequestedNotes();
    708     
    709   if (stopNote(idx)) {
    710     restartANote();
    711   }
    712 }
    713 
    714 static void noteOn(midictrl_t chan, note_t note, midictrl_t vel) {
    715   if (vel == 0) {
    716     noteOff(chan, note, 0);
    717     return;
    718   }
    719 
    720   if (chan == PERC_CHANNEL) {
    721     if (!startPercussion(note)) {
    722       stopOneNote();
    723       startPercussion(note);
    724     }
    725     return;
    726   }
    727     
    728   // Regular note processing now
    729     
    730   if (note < MIDI_MIN || note > MIDI_MAX) {
    731     return; // Just ignore it
    732   }
    733 
    734   ushort idx = note - MIDI_MIN;
    735     
    736   if (m_voiceNo[idx] != NO_VOICE) {
    737     return; // Already playing. Ignore this request.
    738   }
    739 
    740   m_requestMap[idx/8] |= 1 << (idx & 7);
    741   m_velocity[idx] = vel;
    742   m_chan[idx] = chan;
    743   updateRequestedNotes();
    744     
    745   if (!startNote(idx)) {
    746      stopOneNote();
    747      startNote(idx);
    748   }
    749 }
    750   
    751   
    752 static void update100Hz() {
    753   for (ushort i = 0; i < MAX_VOICES; i++) {
    754     voices[i].update100Hz();
    755     if (m_playing[i] == PERC_NOTE && ! (voices[i].isPlaying())) {
    756       m_playing[i] = NO_NOTE;
    757       restartANote();
    758     }        
    759   }
    760 }
    761 
    762 // Main code ----------------------------------------------
    763 
    764 static unsigned long lastUpdate = 0;
    765 
    766 void setup() {
    767   // Hold in reset while we set up the reset
    768   pinMode(nRESET, OUTPUT);
    769   digitalWrite(nRESET, LOW);
    770 
    771   pinMode(clkOUT, OUTPUT);
    772   digitalWrite(clkOUT, LOW);
    773   clockSetup();
    774 
    775   pinMode(BC2_A, OUTPUT);
    776   digitalWrite(BC2_A, LOW); // BC2 low
    777   pinMode(BDIR_A, OUTPUT);
    778   digitalWrite(BDIR_A, LOW); // BDIR low
    779 
    780   pinMode(BC2_B, OUTPUT);
    781   digitalWrite(BC2_B, LOW); // BC2 low
    782   pinMode(BDIR_B, OUTPUT);
    783   digitalWrite(BDIR_B, LOW); // BDIR low
    784 
    785   for (ushort i = 0; i < 8; i++) {
    786     pinMode(dbus[i], OUTPUT);
    787     digitalWrite(dbus[i], LOW); // Set bus low
    788   }
    789 
    790   delay(100);
    791   digitalWrite(nRESET, HIGH); // Release Reset
    792   delay(10);
    793 
    794   lastUpdate = millis();
    795   
    796   psg.init();
    797   for (ushort i = 0; i < MAX_VOICES; i++) {
    798     voices[i].init(i);
    799   }
    800   synth_init();
    801 
    802 #ifdef DEBUG
    803     Serial.begin(115200);
    804 #endif
    805 
    806 #ifdef SERIALMIDI
    807   // Initiate MIDI communications, listen to all channels
    808   MIDI.begin(MIDI_CHANNEL_OMNI);
    809 #endif
    810 }
    811 
    812 void handleMidiMessage(midiEventPacket_t &rx) {
    813   if (rx.header==0x9) {// Note on
    814     noteOn(rx.byte1 & 0xF, rx.byte2, rx.byte3);
    815   }
    816   else if (rx.header==0x8) {// Note off
    817     noteOff(rx.byte1 & 0xF, rx.byte2, rx.byte3);
    818   }
    819   else if (rx.header==0xB) {// Control Change
    820     if (rx.byte2 == 0x78 || rx.byte2 == 0x79 || rx.byte2 == 0x7B) {// AllSoundOff, ResetAllControllers, or AllNotesOff
    821       // Kill Voices
    822       for (ushort i = 0; i < MAX_VOICES; i++) {
    823         voices[i].kill();
    824       }
    825     }
    826   }
    827 }
    828 
    829 void loop() {
    830   midiEventPacket_t rx;
    831 
    832 #ifdef USBMIDI
    833   rx = MidiUSB.read();
    834 
    835 #ifdef DEBUG
    836   //MIDI debugging
    837   if (rx.header != 0) {
    838     Serial.print("Received USB: ");
    839     Serial.print(rx.header, HEX);
    840     Serial.print("-");
    841     Serial.print(rx.byte1, HEX);
    842     Serial.print("-");
    843     Serial.print(rx.byte2, HEX);
    844     Serial.print("-");
    845     Serial.println(rx.byte3, HEX);
    846   }
    847 #endif
    848 
    849   handleMidiMessage(rx);
    850 #endif
    851 
    852 #ifdef SERIALMIDI
    853   //Check for serial MIDI messages
    854   //MIDI.read();
    855   while (MIDI.read()) {
    856     // Create midiEventPacket_t
    857     rx = 
    858       {
    859         byte(MIDI.getType() >>4), 
    860         byte(MIDI.getType() | ((MIDI.getChannel()-1) & 0x0f)), /* getChannel() returns values from 1 to 16 */
    861         MIDI.getData1(), 
    862         MIDI.getData2()
    863       };
    864 
    865 #ifdef DEBUG
    866     //MIDI debugging
    867     if (rx.header != 0) {
    868       Serial.print("Received MIDI: ");
    869       Serial.print(rx.header, HEX);
    870       Serial.print("-");
    871       Serial.print(rx.byte1, HEX);
    872       Serial.print("-");
    873       Serial.print(rx.byte2, HEX);
    874       Serial.print("-");
    875       Serial.println(rx.byte3, HEX);
    876     }
    877 #endif
    878 
    879     handleMidiMessage(rx);
    880   }
    881 #endif
    882 
    883   unsigned long now = millis();
    884   if ((now - lastUpdate) > 10) {
    885     update100Hz();
    886     lastUpdate += 10;
    887   }
    888   
    889   psg.update();
    890 }


