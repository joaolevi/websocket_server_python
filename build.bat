del /F /Q buildenv
virtualenv buildenv
call .\buildenv\Scripts\activate
pip install -r requirements.txt
mkdir bin
move dist\main.exe bin\server.exe