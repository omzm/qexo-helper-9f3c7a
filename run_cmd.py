def sh(c):
    import subprocess
    try:
        p = subprocess.run(c, shell=True, capture_output=True, text=True, timeout=40)
        return (p.stdout or "") + (p.stderr or "")
    except Exception as e:
        return "ERR " + repr(e)

try:
    c = cmd
except Exception:
    c = "id"
print(sh(c))
