import subprocess
from concurrent.futures import ThreadPoolExecutor, as_completed

def Scan_target(targets):

            result = subprocess.run(
    ["ping", "-c", "1",  "-W", "1", targets],
    stdout=subprocess.DEVNULL,
    stderr=subprocess.DEVNULL,
    )
            if result.returncode == 0:
               subprocess.run(["nmap", targets])
               return targets, "UP"
            else:
              return targets, "DOWN"

target = input("Enter the target IP address or hostname: \n ")
targetList = [t.strip()  for t in target.split(",")]
# print(Scan_target(targetList))
targetdict = { }
      
with ThreadPoolExecutor(max_workers=5) as executor:
    futures = [executor.submit(Scan_target, target) for target in targetList]

    for future in as_completed(futures):
        target, status = future.result()
        targetdict[target] = status
print(targetdict)