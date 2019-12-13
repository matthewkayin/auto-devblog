# build.py - This is a script that is meant to build the website using data files
# The idea is to give me the convenience of creating new blog posts without having
# to edit the code and without having to commit to any sort of backend

import os


def open_post(path):
    post_file = open(path, "r")
    post_contents = post_file.read().splitlines()
    post = [post_contents[0], post_contents[1], post_contents[2], []]

    # The format of post is [Shortname, Title, Date, List of lines of content]

    for i in range(3, len(post_contents)):
        post[3].append(post_contents[i])

    return post


def get_post_shortname(post):
    return post[0]


def get_post_title(post):
    return post[1]


def get_post_date(post):
    return post[2]


def get_post_month(post):
    date = get_post_date(post)
    return date[0:date.index(" ")] + " " + date[date.index(", ") + 2::]


def get_post_content(post):
    return post[3]


def create_post_div(post):
    div = []

    content = get_post_content(post)
    div.append("\t\t\t<div class=\"post white\">")
    div.append("\t\t\t\t<p class=\"text headline\">" + get_post_title(post) + "</p>")
    div.append("\t\t\t\t<p class=\"text date\">" + get_post_date(post) + "</p>")
    div.append("\t\t\t\t<p class=\"text content\">" + content[0])
    for i in range(1, len(content) - 1):
        div.append("\t\t\t\t\t\t\t" + content[i])
    div.append("\t\t\t\t\t\t\t" + content[len(content) - 1] + "</p>")
    div.append("\t\t\t</div>")

    return div


def create_month_div(month_list):
    # let's format the month lists as ["Month YYYY", [Title, shortname], ...]
    # this way we only store the month once but we still get a list
    div = []

    div.append("\t\t\t<div class=\"post white\">")
    div.append("\t\t\t\t<p class=\"text headline\">" + month_list[0] + "</p>")
    for i in range(1, len(month_list)):
        div.append("\t\t\t\t<p class=\"text content\"><a href=\"" + month_list[i][1] + ".html\">" + month_list[i][0] + "</a></p>")
    div.append("\t\t\t</div>")

    return div


def create_from_template(template_path, dest_path, divs):
    template_file = open(template_path)
    template = template_file.read().splitlines()

    output = template[0:template.index("REPLACE")]
    for div in divs:
        output = output + div
    output = output + template[template.index("REPLACE") + 1::]

    post_file = open(dest_path, "w")
    post_file.writelines("\n".join(output))


print("Hello! Welcome to the extremely specific blog compiler!")
print("Compiling website...")
recent_posts = []
month_lists = []

num_posts = len([name for name in os.listdir("posts") if os.path.isfile("posts/" + str(name))])
for i in range(0, num_posts):
    post_num = i + 1
    post_file = "posts/" + str(post_num) + ".txt"
    print("Reading " + post_file + "...", end=" ")
    post = open_post(post_file)

    shortname = get_post_shortname(post)
    title = get_post_title(post)
    month = get_post_month(post)

    # If current post's month in list add the post to the list
    # else create a new month list for this month
    if month in [month_list[0] for month_list in month_lists]:
        location = [month_list[0] for month_list in month_lists].index(month)
        month_lists[location].insert(1, [title, shortname])
    else:
        month_lists.append([month, [title, shortname]])

    div = create_post_div(post)

    if len(recent_posts) < 10:
        recent_posts.insert(0, div)
    else:
        recent_posts.pop()
        recent_posts.insert(0, div)

    create_from_template("article.html", shortname + ".html", [div])
    print("Done!")

print("Generating index...", end=" ")
create_from_template("index-template.html", "index.html", recent_posts)
print("Done!")

print("Generating archive...", end=" ")
month_divs = []
for month_list in month_lists:
    month_divs.insert(0, create_month_div(month_list))

create_from_template("archive-template.html", "archive.html", month_divs)
print("Done!")

print("Website build complete! Maybe use wordpress next time?")
