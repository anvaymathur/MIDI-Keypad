# MIDI-Keypad

MIDI Keypad built for Half Life from HackClub. It is hackpad that uses copper touch pads 
that act as buttons for playing notes. A rotary encoder is used to control the octave of the notes.
It can also act like a normal macropad if you chose to, just push down the encoder to switch modes.
The encoder will then act as volume control and the copper touch pads will act like your macro keys.

## Description

This was built following the guide provided by Half Life Hack Club for their music week project. It was a fun
project to make to learn more about music in general because I have never done many music related things before
so learning how MIDI works and how to use it to create music was fun. I added the macropad feature to make it
more functional for me as I do not often create music.

## Features

- Custom PCB
- Neopixel Lights for mode status and while playing notes
- OLED Screen for displaying information
- Copper Touch Pads formed in the shape of a hand to act like ergonomic keys
- EC11 Rotary Encoder for octave control
- Switch modes to use as a generic macropad

## PCB

Custom PCB Made in KiCad. Some footprints and schematics were from Kai Pereira's 
[Hackclub-KiCad-Libraries]("https://github.com/KaiPereira/Hackclub-KiCad-Libraries")

![FinishedSchematic](assets\FinishedSchematic.png)
![PCB3D](assets\PCB3D.png)
![PCB(1)](assets\PCB(1).png)

## Firmware

There is custom firmware written in CircuitPython for controlling all of the components, currently does not include code for different modes, only for the main music mode.

## [BOM](https://docs.google.com/spreadsheets/d/1wcF_mPrZf543xQacLG9ci4BRGrGUtqLDjnGJwcqraqM/edit?usp=sharing)
| Item  | Description | # of Sets | #Pcs / Set | Price / Set (USD) | Item Total Price + Tax & Shipping (USD)| Supplier | URL|
| ----- | ----------- | --------- | ---------- | ----------------- | -------------------------------------- | -------- | -------|
| Megaboard PCB Printing with JLCPCB | PCB | 1 | 5 | $4.00 | $11.33 | JLC PCB | https://kommodo.ai/i/mOOA8IN1I4RNeobWpcTo |
| Waveshare ESP32-S3-Zero | Microcontroller | 1 | 1 | $8.25 | $8.25 | Aliexpress | https://www.aliexpress.com/item/1005012733231291.html?spm=a2g0o.productlist.main.1.47f356e3O78umQ&algo_pvid=a33f782b-47fe-45dc-9786-74fe5942f79a&algo_exp_id=a33f782b-47fe-45dc-9786-74fe5942f79a-0&pdp_ext_f=%7B%22order%22%3A%2263%22%2C%22spu_best_type%22%3A%22price%22%2C%22eval%22%3A%221%22%2C%22fromPage%22%3A%22search%22%7D&pdp_npi=6%40dis%21CAD%2112.18%213.95%21%21%218.50%212.76%21%402101e80f17928740388593327e0f82%2112000059219676552%21sea%21CA%210%21ABX%211%210%21n_tag%3A-29910%3Bd%3Adfeb2caa%3Bm03_new_user%3A-29895%3BpisId%3A5000000218625932&curPageLogUid=9dLDZeafbhZQ&utparam-url=scene%3Asearch%7Cquery_from%3A%7Cx_object_id%3A1005012733231291%7C_p_origin_prod%3A |
| Rotary Encoder EC11 | Rotary Encoder | 1 | 1 | $1.98 | $1.98 | Aliexpress | https://www.aliexpress.com/item/1005006127287538.html?spm=a2g0o.productlist.main.6.14e7639e1W7sGD&algo_pvid=d787a78f-ca16-4b24-b78e-9b4ec4559ee3&algo_exp_id=d787a78f-ca16-4b24-b78e-9b4ec4559ee3-5&pdp_ext_f=%7B%22order%22%3A%22562%22%2C%22eval%22%3A%221%22%2C%22fromPage%22%3A%22search%22%7D&pdp_npi=6%40dis%21USD%212.70%210.99%21%21%212.70%210.99%21%402103094f17928742152533599e100f%2112000035878244634%21sea%21CA%210%21ABX%211%210%21n_tag%3A-29910%3Bd%3Adfeb2caa%3Bm03_new_user%3A-29895%3BpisId%3A5000000218625932&curPageLogUid=TQRes1uqiTr3&utparam-url=scene%3Asearch%7Cquery_from%3A%7Cx_object_id%3A1005006127287538%7C_p_origin_prod%3A |
| SK6812 MINI-E RGB | LED | 1 | 100 | $4.29 | $4.29 | Aliexpress | https://www.aliexpress.com/item/1005007576573654.html?spm=a2g0o.productlist.main.2.1b29677eKDjWdF&algo_pvid=cd1006e3-d410-4b66-8223-8e53e4b6af3e&algo_exp_id=cd1006e3-d410-4b66-8223-8e53e4b6af3e-1&pdp_ext_f=%7B%22order%22%3A%2263%22%2C%22spu_best_type%22%3A%22price%22%2C%22eval%22%3A%221%22%2C%22fromPage%22%3A%22search%22%7D&pdp_npi=6%40dis%21USD%214.29%210.99%21%21%2128.48%216.58%21%402103129017928745977964237e0c7b%2112000061041866515%21sea%21CA%210%21ABX%211%210%21n_tag%3A-29910%3Bd%3Adfeb2caa%3Bm03_new_user%3A-29895%3BpisId%3A5000000218625932&curPageLogUid=jyd2w9d4CFqN&utparam-url=scene%3Asearch%7Cquery_from%3A%7Cx_object_id%3A1005007576573654%7C_p_origin_prod%3A |
| 0.96 in OLED IIC Serial Display Module | OLED Screen | 1 | 1 | $2.68 | $2.68 | Aliexpress | https://www.aliexpress.com/item/1005006141235306.html?spm=a2g0o.productlist.main.1.29c26b0firbgYR&algo_pvid=ea3a9a18-0200-463a-9fe7-0c7b90465e07&algo_exp_id=ea3a9a18-0200-463a-9fe7-0c7b90465e07-0&pdp_ext_f=%7B%22order%22%3A%2226226%22%2C%22spu_best_type%22%3A%22price%22%2C%22eval%22%3A%221%22%2C%22fromPage%22%3A%22search%22%7D&pdp_npi=6%40dis%21USD%212.68%211.19%21%21%2117.80%217.91%21%4021030f4a17928748570274353e0f9c%2112000035944225407%21sea%21CA%210%21ABX%211%210%21n_tag%3A-29910%3Bd%3Adfeb2caa%3Bm03_new_user%3A-29895%3BpisId%3A5000000218625933&curPageLogUid=2CvgUD0ixaiQ&utparam-url=scene%3Asearch%7Cquery_from%3A%7Cx_object_id%3A1005006141235306%7C_p_origin_prod%3A |
| Single Row Female 2.54mm Pinheader Connector | OLED Socket | 1 | 50 | $3.15 | $3.15 | Aliexpress |  https://www.aliexpress.com/item/1005003610378386.html?spm=a2g0o.productlist.main.12.4c5b53814XmSqi&algo_pvid=86a08817-bda5-4dd8-8af6-afcc5c2f45a8&aem_p4p_detail=2026102414242814665487072167430000800614&algo_exp_id=86a08817-bda5-4dd8-8af6-afcc5c2f45a8-11&pdp_ext_f=%7B%22order%22%3A%22948%22%2C%22eval%22%3A%221%22%2C%22fromPage%22%3A%22search%22%7D&pdp_npi=6%40dis%21USD%213.65%211.65%21%21%213.65%211.65%21%402101ca8b17928770687123570e0d8a%2112000026598176397%21sea%21CA%210%21ABX%211%210%21n_tag%3A-29910%3Bd%3Adfeb2caa%3Bm03_new_user%3A-29895%3BpisId%3A5000000218656158&curPageLogUid=8YnDUKAVvz2Y&utparam-url=scene%3Asearch%7Cquery_from%3A%7Cx_object_id%3A1005003610378386%7C_p_origin_prod%3A&search_p4p_id=2026102414242814665487072167430000800614_3 |
| **Grand Total** | *$31.68* 