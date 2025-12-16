#write a program to create a dictionary of hindi words with 
# values as their english translation.provide user with an option to look it up!


words={
    "madad":"help",
    "kursi":"chair",
    "ghoda":"horse"
}

word =input("enter the word you want meaning of: ")

print(words[word])
print(words.get(word, "Word not found in dictionary"))