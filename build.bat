rm -r buildenv
python3 -m virtualenv buildenv
. "./buildenv/bin/activate"
pip install -r requirements.txt