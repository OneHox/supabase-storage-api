import os
import base64
import shutil
from supabase import create_client, Client

src = "source"
zip = "source.zip"
b64 = "source.b64"

key: str = os.environ.get("SUPABASE_KEY")
url: str = os.environ.get("SUPABASE_URL")
bkt: str = os.environ.get("BUCKET_NAME")
pth: str = os.environ.get("ASSETS_PATH")
supabase: Client = create_client(url, key)


def clean():
    if os.path.exists(zip):
        os.remove(zip)
    if os.path.exists(b64):
        os.remove(b64)
