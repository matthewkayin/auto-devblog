import os

dont_delete = ["about.html", "index-template.html", "archive-template.html", "article.html", "build.py", "clean.py", ".flake8"]

print("Cleaning up directory...")
for name in os.listdir("."):
    if os.path.isfile(name) and name not in dont_delete:
        print("Deleting " + name + ".")
        os.remove(name)

print("Done!")
