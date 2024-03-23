import time


def initboard():
    combine = ""
    board = open("Letter Boxed\\Words\\letter boxed diagram.txt", "r")
    side = None
    top = set()
    left = set()
    right = set()
    bottom = set()
    for line in board:
        line = line.strip()
        if line:
            if line not in {"top", "bottom", "left", "right"}:
                combine += str(line)
            if line in ["top", "left", "right", "bottom"]:
                side = line
            elif side:
                for char in line:
                    if side == "top":
                        top.add(char)
                    elif side == "left":
                        left.add(char)
                    elif side == "right":
                        right.add(char)
                    elif side == "bottom":
                        bottom.add(char)

    alpha_vector = 0
    for char in combine:
        alpha_vector |= 1 << ord(char) - ord("a")

    return top, left, right, bottom, alpha_vector


def checkpos(x, top, left, right, bottom):
    if x in top:
        temp = top
    elif x in left:
        temp = left
    elif x in right:
        temp = right
    elif x in bottom:
        temp = bottom
    else:
        temp = None
    return temp


def precompute_bit_vector(word):
    bit_vector = 0
    for char in word:
        bit_vector |= 1 << (ord(char) - ord("a"))
    return bit_vector


def word_check(line):
    for i in range(1, len(line)):
        if line[i] in checkpos(line[i - 1], top, left, right, bottom):
            return False
    return True


def get_words():
    with open("Letter Boxed\Words\wordlist.txt", "r") as file:
        return [line.strip() for line in file]


start = time.time()
Words = []

top, left, right, bottom, alpha_vector = initboard()

wordlist = get_words()


for line in wordlist:
    line = line.strip()
    if (precompute_bit_vector(line) | alpha_vector) == alpha_vector:
        if word_check(line):
            Words.append(line)

print(f"Found {len(Words)} letterboxed words\n\nSorting the list...")
Words.sort(key=len, reverse=True)

with open(r"Letter Boxed\Words\LongestWords.txt", "w") as file:
    for line in Words:
        file.write(line + "\n")

print("Done! You can find the words at Letter Boxed\Words\LongestWords.txt")

end = time.time()
execution_time = end - start
print(f"Execution time: {execution_time} seconds")
