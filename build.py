# build.py - This is a script that is meant to build the website using data files
# The idea is to give me the convenience of creating new blog posts without having
# to edit the code and without having to commit to any sort of backend


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
    div.append("""\t\t\t<div class="post white">""")
    div.append("""\t\t\t\t<p class="text headline">""" + get_post_title(post) + "</p>")
    div.append("""\t\t\t\t<p class="text date">""" + get_post_date(post) + "</p>")
    div.append("""\t\t\t\t<p class="text content">""" + content[0])
    for i in range(1, len(content) - 1):
        div.append("\t\t\t\t\t\t\t" + content[i])
    div.append("\t\t\t\t\t\t\t" + content[len(content) - 1] + "</p>")
    div.append("""\t\t\t</div>""")

    return div


def create_post_file(shortname, div):
    template_file = open("article.html", "r")
    template = template_file.read().splitlines()

    output = template[0:template.index("REPLACE")] + div + template[template.index("REPLACE") + 1::]
    post_file = open(shortname + ".html", "w")
    post_file.writelines("\n".join(output))


# test some stuff
post = open_post("posts/1.txt")
shortname = get_post_shortname(post)
month = get_post_month(post)
div = create_post_div(post)
create_post_file(shortname, div)
print(month)
