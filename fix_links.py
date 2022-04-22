from os import listdir
from os.path import join
from subprocess import run

def get_input(message):
    while True:
        inp = input(message)
        if inp[:1] in "yYnN":
            return inp[:1] in "yY"

def main():
    for filename in listdir("docs"):
        if filename.startswith(".") or not filename.endswith(".html") or filename.startswith("index") or filename == "calendar.html":
            continue
        with open(join("docs", filename)) as f:
            content = f.read()
            if "nav-links" not in content:
                continue
            missing = []
            if "nav-previous" not in content:
                missing.append("previous")
            if "nav-next" not in content:
                missing.append("next")
            if missing:
                print(filename, "missing", ", ".join(missing))
                if get_input("Fix? (y/N): "):
                    run(["make", "-B", join("docs", filename)])

if __name__ == "__main__":
    main()
