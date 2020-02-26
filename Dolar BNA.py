import urllib

page = urlopen("https://ae7.st/g/")

contents = page.read()

page.close()

print(contents)
