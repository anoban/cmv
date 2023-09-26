import os

contents: list[str] = []

for file in os.listdir(r"D:/cmv/data/refseqs/edited/"):
    if file.endswith(".fasta"):
        with open(r"D:/cmv/data/refseqs/edited/" + file, 'r') as fp:
            text = str(fp.read())
            contents.append(text)
            contents.append("\r\n")
        
with open(r"D:/cmv/data/refseqs/edited/sdt.fasta", 'w') as fp:
    for cont in contents:
        fp.write(cont)