# Flashing Instructions

---

Follow these steps to install KMK firmware on your nice!nano MCU:

1. Connect your nice!nano to your PC using a Type-C cable.
2. It will mount as a USB drive on your system.
3. Download the CircuitPython `.UF2` file for the nice!nano from:
   `https://circuitpython.org/board/nice_nano/`
4. Drag and drop the `.UF2` file onto the nice!nano drive.
   It will flash automatically, eject itself, and remount as `CIRCUITPY`.
5. Download the KMK firmware from `https://github.com/KMKfw/kmk_firmware`.
6. Copy the `kmk/` folder and your `code.py` into the root of the `CIRCUITPY` drive.
7. The MCU will execute `code.py` automatically on the next boot.
   Your keyboard should now be fully functional.

> **Note:** If the keyboard is unresponsive, double-tap the Reset button to re-enter
> bootloader mode and repeat from step 3.

---