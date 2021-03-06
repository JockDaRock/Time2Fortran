import sys
import os
from io import StringIO
import contextlib
import subprocess


@contextlib.contextmanager
def stdoutIO(stdout=None):
    old = sys.stdout
    if stdout is None:
        stdout = StringIO()
    sys.stdout = stdout
    yield stdout
    sys.stdout = old


def get_stdin():
    buf = ""
    for line in sys.stdin:
        buf = buf + line
    return buf


if __name__ == "__main__":
    st = get_stdin()
    # print(st)
    with stdoutIO() as s:
        try:
            tmpfile = "/root/main.f95"
            # print(tmpfile)
            f = open(tmpfile, 'w')
            print(st, file=f)
            f.close()
            p0 = subprocess.Popen(["gfortran", tmpfile, "-o", "main"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            p4, p5 = p0.stdout.read().decode('utf-8'), p0.stderr.read().decode('utf-8')
            if len(p4) > 0:
                print(p4)
            elif len(p5) > 0:
                print(p5)

            p1 = subprocess.Popen(["/root/main"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            p2, p3 = p1.stdout.read().decode('utf-8'), p1.stderr.read().decode('utf-8')
            if len(p2) > 0:
                print(p2)
            else:
                print(p3)
        except BaseException as e:
            print(e)
    print(s.getvalue())
