import pyshorteners
link = input("enter link here :")
shortener=pyshorteners.Shortener()
x = shortener.tinyurl.short(link)
print(x)
