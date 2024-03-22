from common import *

if not (os.path.exists(src)):
    print("Source directory not present!")
else:
    clean()
    zips = zip.split(".")
    shutil.make_archive(zips[0], zips[1], src)

    with open(zip, 'rb') as compressed:
        compress_data = compressed.read()

    ready = base64.b64encode(compress_data).decode('utf-8')
    with open(b64, 'w') as handle:
        handle.write(ready)
        handle.close()

    supabase.storage.from_(bkt).remove(f'{pth}/source.b64')
    supabase.storage.from_(bkt).upload(file=b64, path=f'{pth}/source.b64', file_options={"content-type": "text/plain", "x-upsert": "true", "cache-control": "3600"})
    clean()
