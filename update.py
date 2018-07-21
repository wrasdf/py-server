from pathlib import Path

filename = "test.cert"
contents = Path(filename).read_text()
contentsNew = contents.replace('\n', '\\n')

Path("nex.txt").write_text(contentsNew)

# with open("new.txt", "w") as text_file:
#     print(f"{contentsNew}", file=text_file)
