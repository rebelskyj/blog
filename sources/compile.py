from sys import argv, exit, stderr
import subprocess
import shlex

def main():
    if argv[1].startswith("docs/"):
        filename = argv[1].partition("docs/")[2].replace(".html", "")
    else:
        # We've been given a line from sources/order.txt
        filename = argv[1].split(":")[0].replace(".tex", "")
    with open("sources/order.txt") as order:
        prev = ":"
        lines = iter(order)
        for i, line in enumerate(lines):
            if line.startswith(f"{filename}.tex:"):
                break
            prev = line
        else:
            print(f"Couldn't find `{filename}` in sources/order.txt")
            exit(1)
        try:
            next_ = next(lines)
        except StopIteration:
            next_ = ":"

    source = f"sources/{filename}.tex"
    dest = f"docs/{filename}.html"

    name = line.split(":")[1]
    prev_url, prev_name = prev.split(":")
    next_url, next_name = next_.split(":")
    next_url = next_url.replace(".tex", ".html")
    prev_url = prev_url.replace(".tex", ".html")

    options = {
        "next": next_name,
        "prev": prev_name,
        "nexturl": next_url,
        "prevurl": prev_url,
        "pagetitle": name
    }

    command = [
        "pandoc",
        source,
        "-s", "-o", dest,
        "--template=sources/template.html",
        "--css", "pandoc.css"
    ]

    for key, val in options.items():
        key, val = key.strip(), val.strip()
        if val:
            command += ["-M", f"{key}={val}"]

    print(f"Running `{shlex.join(command)}`")
    subprocess.run(command)


if __name__ == "__main__":
    main()
