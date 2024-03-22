from common import *

try:
  res = supabase.storage.from_(bkt).download(f'{pth}/{b64}')
  if res:
    clean()
    with open(zip, 'wb+') as z:
      z.write(base64.b64decode(res))
      z.close()
      if os.path.exists(src):
        shutil.rmtree(src)
      try:
        shutil.unpack_archive(zip, src)
      except Exception as e:
        print(f"Error extracting '{zip}': {e}")
    clean()
except Exception as e:
  print(f"Downloading '{pth}/{b64}': {e}")
