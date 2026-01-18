# ModuPad v2
<img width="3593" height="2464" alt="ModuPad_v2_Sketch-PNG-Dark-Mode_3xScale_ excalidraw" src="https://github.com/user-attachments/assets/7e46cdf8-0388-4e83-94f7-2fd80c8edda1" />
---
>  Presenting [ModuPad v2](https://github.com/lassiipk/ModuPad_v2) improved version of [ModuPad v1](https://github.com/lassiipk/ModuPad) with 5x5 (25 keys) Macro-Focused, 3 Encoders with push buttons, nice!nano display for visuals and animations, and an nice!nano MCU for pin constraints and simplify design

---
## Planning

- The project began with a review of my [ModuPad V1](https://github.com/lassiipk/ModuPad) project, built using a Seeed XIAO RP2040, including a 3×3 key matrix, one rotary encoder, and an OLED display.
- I was planning on 4x4 key matrix, two (2) encoders, each key with addressable LEDs, and an OLED diplay, But as the project evolved I was limited and forced on using the current ModuPad features (mentioned above).
- Based on XIAO RP2040 pins, I was limited on adding more to my PAD, then i decided that the XIAO RP2040 could not realistically support the desired V2 feature set without expanders.
- Then I chose to move away from the XIAO RP2040 and select the nice!nano instead, for my [V2 ModuPad](https://github.com/lassiipk/ModuPad_v2).
- The new V2 hardware plan I proposed is as under:
  - nice!nano (MCU)
  - 5×5 key matrix (25 keys)
  - 3 encoders with push buttons
  - nice!view display
  - Addressable LEDs under each switch key
  - Hot-swap sockets
  - 1800 mAh Li-ion battery
  - Bluetooth wireless operation
 
> I decided that LEDs and the nice!view display would only be used in wired mode.
>
> Wireless mode would disable LEDs and the display to preserve battery life.

---

## Constraints

- XIAO RP2040 will not be used for V2 (limits me from adding more features into V2.
- nice!nano was chosen to reduce pin constraints and simplify design (Gives me alot of room to add more features in V2).
- V2 will use a 5×5 key matrix (Macro-Focused).
- V2 will include 3 rotary encoders with push buttons (For modularity).
- Each key will have an addressable LED for aesthetics and visuals (Because why not? LEDs are Cool Man, I love them as its make things easir when using keys in Night as the lights are off and you cant see shit! And imagin you could set cool modes that changes its Color and hue automatically).
- Hot-swap sockets will be used for all keys as it removes the hassel of sottring the key switches on the PCB, by using Hot-swap it makes things easir when cleaning and replacing a different key switch.
- nice!view will be used as the display to replace ModuPad-V1 "I²C like SSD1306" - 0.91 inc OLED Display
- A 3.7V 1800 mAh battery will be included.
- Bluetooth will be used for wireless operation (for modularity).
- LEDs and nice!view will be disabled during battery operation (to save battery power).
- LEDs and nice!view will only be active during wired (USB) operation (Again to save battery).

---

## Knowledge Gained

- Firmware is software that defines how hardware behaves and communicates with the computer.
- Mechanical switches bounce electrically when pressed.
- Debouncing filters unstable signals caused by switch bounce.
- Ghosting is caused by unintended current paths in a key matrix.
- Diodes prevent ghosting by enforcing one-way current flow.
- Key matrices reduce GPIO usage by organizing keys into rows and columns.
- Addressable LEDs require only one data pin (GPIO) regardless of LED count.
- Displays and LEDs are major contributors to power consumption (IN BATTERY/BLUETHOOT MODE).

---

## Project Status

- [ModuPad V2](https://github.com/lassiipk/ModuPad_v2) currently in planning phase.
- Architecture decisions made so far are recorded.

---

> ***I'm currently in planing phase, that can improve my fisrt project ([ModuPad](https://github.com/lassiipk/ModuPad)) in both physically and theoretically sector of the main project.
The main goal of this project ([ModuPad V2](https://github.com/lassiipk/ModuPad_v2)) is to improve my electronics and improve my [ModuPad V1](https://github.com/lassiipk/ModuPad) as much as I can, and learn electronic by building this MacroPAD from scratch with having ZERO knowlage on electronic.***

` *Everything written in this journal took me about 2-3 hours to research, learn and write it down in this jornal and log everything!* `

---

> ***Project Start Date:*** 05-JAN-2026 | 3:40_PM (After submitting MODUPAD_v1)
> ***Project Progress Status Record:*** Everything written in this Journal is the proof of what i've learnd and accomplised so far! 18-JAN-2026 | 9 PM
> ***Project Journal Submit Date:*** 18-JAN-2026 | 10 PM ( Why this much GAP between Peoject_Start_Date_ AND Project_Journal_Submit_Date ??? Answer: I was busy with other things for example: Studies. Gaming and other personal stuff!!!)

