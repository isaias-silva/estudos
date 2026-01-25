import subprocess


def sync_on_github():
    print("sync on github...")

    result = subprocess.run(["git", "status"], capture_output=True, text=True)

    if "add" in result.stdout:
        message = get_commit_description()

        subprocess.run(["git", "add", "."])
        subprocess.run(["git", "commit", "-m", message])
        subprocess.run(["git", "push"])

def get_commit_description():
    return "automatic adition"

sync_on_github()
