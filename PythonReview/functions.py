
def python_food():
    width = 80
    text = "Spam and eggs"
    left_margin = (width - len(text)) // 2
    print(" " * left_margin, text)

def centre_text(*args, sep=" ", end='\n', file=None, flush=False):
    text = ""
    for arg in args:
        text += str(arg) + sep
    left_margin = (80 - len(text)) // 2
    print(" " * left_margin, text, end=end, file=file,flush=flush)

centre_text("spam and egggs")
centre_text("spam, spam and egggs")
centre_text("spam, spam, spam and egggs")
centre_text(100)

print(python_food()) #they return None if you don't specify a return

centre_text("Three", "Two", "One", 1, 2, sep=": ")
print()

