import os
import tempfile
import datetime
import shutil

temp_dir = tempfile.mkdtemp()

now = datetime.datetime.now()
for f in os.listdir(temp_dir):
    f_path = os.path.join(temp_dir, f)
    if os.path.getmtime(f_path) < (now - datetime.timedelta(days=1)).timestamp():
        shutil.rmtree(f_path)