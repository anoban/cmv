import os

contents: list[str] = []

for file in os.listdir(r"D:/cmv/data/seqs/edited/"):
    if file.endswith(".fa"):
        with open(r"D:/cmv/data/seqs/edited/" + file, 'r') as fp:
            text = str(fp.read())
            contents.append(text)
            contents.append("\r\n")
        
with open(r"D:/cmv/data/seqs/edited/sdt.fasta", 'w') as fp:
    for cont in contents:
        fp.write(cont)