import subprocess
import re
import ai
from dotenv import load_dotenv

load_dotenv()


def sync_on_github():
    print("sync on github...")

    result = subprocess.run(["git", "status", "-sb"], capture_output=True, text=True)

    if "M" in result.stdout or "??" in result.stdout:
        message = get_commit_description(result.stdout)

        subprocess.run(["git", "add", "."])
        subprocess.run(["git", "commit", "-m", message])
        subprocess.run(["git", "push"])


def get_commit_description(output: str):
    updateds = re.findall(r"(?<=M ).+", output)
    createds = re.findall(r"(?<=\?\?).+", output)

    changes = "crie uma mensagem com o resumo das mudanças ocorridas:\n"
    for update in updateds:
        changes += "diff de arquivo existente:\n" + get_diff(update)

    for created in createds:
        changes += "diff de arquivo adicionado:\n" + get_diff(created)

    message = ai.getCommitMessageWithAI(changes)

    return message


def get_diff(path: str):
    diff_exec = subprocess.run(
        ["git", "--no-pager", "diff", path], capture_output=True, text=True
    )

    return diff_exec.stdout


sync_on_github()
