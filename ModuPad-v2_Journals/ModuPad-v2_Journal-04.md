## Finished with PCB Design

<img width="765" height="1031" alt="Screenshot 2026-01-23 115402" src="https://github.com/user-attachments/assets/30a17647-1b5f-4cb9-af9d-6b80a30d69e5" />

Fully complete my PCB design today, PHEW that was a time sink. Had to dig through so many resources online just to get everything right, but it’s finally done. The design is completely based on the sketch from my first journal, including the 5×5 key matrix (Cherry MX style switches) with each Kilah Hotswap socket and each key having its own LED (SK6812MINI-E).

Also added 3 encoders with push buttons — no LEDs underneath them — each with a specific role: one to change the nice!view display mode, another for messing with the switch LEDs (hue, modes, etc.), and the last to interact with the OS (volume, global mute/deafen). The display (nice!view) is fully integrated for visuals, loop animations, status, and text — controllable via keys or encoders depending on user preference.

The MCU (nice!nano) is set up for flashing via ZMK for Bluetooth connectivity and all the other firmware features. Honestly, it’s wild how much can be achieved from this tiny device.

It took me over 2 days straight — I started right after finishing the schematic and didn’t even realize how much time had passed. I got so deep into the PCB that I skipped games, studies, and even meals. Crazy how focused I got.

---

## Timeline

- Start: ~6:00 PM — 21 Jan 2026
- End: 12:00 PM — 23 Jan 2026
- Journal entry written: ~12:30 PM — 23 Jan 2026

*Planned continuation: Work on the project’s CAD case, improving a lot of things for this new version, really looking forward to it.*

## Current Status

- 5×5 key matrix finalized (Cherry MX style switches, each with Kilah Hotswap socket).
- Each key has its own LED (SK6812MINI-E).
- 3 encoders with push buttons (no LEDs), each assigned specific control functions.
- Display (nice!view) fully integrated, controllable via keys and encoders.
- MCU (nice!nano) ready for ZMK flashing and Bluetooth functionality. 
- PCB layout fully matches the original sketch from the first journal.

> Next up: CAD case design. Excited to start improving this version.

## 📸 Images
| Front | Front-Side |Back-Side| Back |
|-------|-------|-------|-------|
| <img width="1724" height="930" alt="ModuPad_v2_Front" src="https://github.com/user-attachments/assets/d1b20612-6670-4c93-aa06-64e31960b061" /> | <img width="1724" height="930" alt="ModuPad_v2_Front-Side" src="https://github.com/user-attachments/assets/29a5e9e0-a927-43a1-a7b3-faa234a0cb0e" /> | <img width="1724" height="930" alt="ModuPad_v2_Back-Side" src="https://github.com/user-attachments/assets/e5ccf7ea-7c32-4543-9455-4ae480702e27" /> | <img width="1724" height="930" alt="ModuPad_v2_Back" src="https://github.com/user-attachments/assets/6f3e5a19-605f-421f-a97d-0c34fb34f53b" /> |
