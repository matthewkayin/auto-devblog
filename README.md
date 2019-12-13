# auto-devblog
This is my devblog! I created it because I decided that I wanted to make a game once winter break started, and I wanted to make a devblog of the game as I made it. Also I'm rusty at HTML / CSS so this was a good refresh of the stuff that I do know.

This blog is a static site built in pure HTML / CSS. There's not a single line of javascript here. I went for a very minimal site design and it's not the prettiest but the code is something I can build off of if I ever want this to be more than what it is. 

## A compiled website

What I'm most proud of about this site are the python scripts. They're the reason the repo is called *auto*-blog.

The big one is build.py, it takes the HTML template files I've created and then generates unique HTML files for the blog by using the /posts/ folder to get the blog's content. This way all I have to do is edit the posts in the /posts/ folder and the changes I make to the posts will be reflected on in the entirety of the blog without me having to update changes across each file. 

Specifically, the index.html file will always contain the ten most recently created posts, the archive file will contain links to every post on the blog (organized by month and year), and each post will have its own html page that can be linked to.

Meanwhile there's also a clean.py script, which can be ran to clear out all non-necessary (generated) files so that I can work without a bunch of small HTML files in the way (it's sort of like a "make clean").

## Why do this?

I wanted the long-term ease-of-use provided by something like Wordpress but I also wanted to do my own coding when making this devblog, and I also didn't want to have to host my own webserver or pay someone to do it for me. So I decided to host the site in github pages and make a script to save me the effort of fiddling with HTML files. And so here we are.
