import random

def get_user_input():
    print(" ")
    print("---- Auto Nickname Combiner ----")
    first_name = input("First name : ").strip()
    last_name = input("Last name : ").strip()
    return first_name, last_name

def generate_basic_nicknames(first, last):
    return [
        first[:3] + last[-3:],
        first[:2] + last[:2],
        last[:3] + first[-2:],
        first + last[0]
    ]

def add_creative_variants(nicknames):
    creative = []
    symbols = ['_', '@', '99', 'X', '#', '!', '$', '786']
    for name in nicknames:
        creative.append(name.capitalize() + random.choice(symbols))
        creative.append(name.upper())
        creative.append(name.lower() + str(random.randint(1, 100)))
    return creative

def filter_by_style(nicknames, style):
    if style == "short":
        return [n for n in nicknames if len(n) <= 6]
    elif style == "fun":
        return [n for n in nicknames if any(c in n for c in "_#X!")]
    elif style == "formal":
        return [n for n in nicknames if n.isalpha()]
    return nicknames

def display_nicknames(nicknames):
    print("\n----- Your Nicknames -----")
    for nick in nicknames:
        print(f"- {nick}")
    print("------------------------")

def save_to_file(nicknames):
    with open("saved_nicknames.txt", "w") as f:
        for nick in nicknames:
            f.write(nick + "\n")
    print("Nicknames saved to 'saved_nicknames.txt'.")

def main():
    first, last = get_user_input()
    base = generate_basic_nicknames(first, last)
    creative = add_creative_variants(base)
    all_nicknames = base + creative

    style = input("Nickname style (Short / Fun / Formal / Any): ").strip().lower()
    filtered = filter_by_style(all_nicknames, style)

    display_nicknames(filtered)

    if input("Save to a file? (Yes / No): ").strip().lower() == "yes":
        save_to_file(filtered)

if __name__ == "__main__":
    main()
