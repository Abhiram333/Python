import webbrowser, time
import subprocess
import random
n = random.randint(15,45)
time.sleep(n)
url = "https://youtu.be/mm3kPaZ99Po"
for i in range(1):
    webbrowser.open_new(url)
    time.sleep(30)

cmd = 'python3 SabatogeTimer.py'
p = subprocess.Popen(cmd, shell = True)
out, err = p.communicate()
print(err)
print(out)


