rm -r buildenv
virtualenv buildenv
call .\buildenv\Scripts\activate
pip install -r requirements.txt