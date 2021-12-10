print()

print("This word counter assumes there will be exactly one space between each word, no spaces before the first word, and no spaces after the last word.\n")

text = input("Enter some text:\n")
count = 0

for character in text:
  if character == " ":
    count = count + 1

print(f"\nWord count: {count + 1}")
