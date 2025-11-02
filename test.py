from os import scandir

md_files = scandir("D:/PKM/0_inbox")
feed = []

for i in md_files:
    feed.append(i)

# for note in feed:
#     print(note.name)
#     print(note.path)

with open(feed[0].path, encoding="utf-8") as f:
    read_data = f.read()

print(read_data)