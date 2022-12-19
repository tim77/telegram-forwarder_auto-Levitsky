cls
timeout /t 50
:start
python.exe telegram-forwarder_auto-Levitsky.py
timeout /t 30
goto start
