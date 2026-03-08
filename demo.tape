# blefyi — Python BLE API Client Demo
Output demo.gif

Set FontSize 20
Set Width 1000
Set Height 560
Set Shell "zsh"
Set Theme "Catppuccin Mocha"
Set TypingSpeed 30ms
Set Padding 24

Type "uv run --with blefyi python3"
Enter
Sleep 2s

Type "from blefyi import BLEFYI"
Enter
Sleep 1s

Type "client = BLEFYI()"
Enter
Sleep 1s

Type "# Search BLE chips"
Enter
Sleep 0.5s

Type "client.search('nordic')"
Enter
Sleep 2.5s

Type "# Look up a BLE chip"
Enter
Sleep 0.5s

Type "client.chip('nrf52840')"
Enter
Sleep 3s

Type "exit()"
Enter
Sleep 1s
