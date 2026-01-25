import subprocess


def sync_on_github():
    print("sync on github...")
    
    result = subprocess.run(["git", "status"], capture_output=True, text=True)

        
       

sync_on_github()
