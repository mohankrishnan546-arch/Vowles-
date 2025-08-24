def count_vowels_consonants(s):
    vowels = "aeiou"
    s = s.lower()   
    vowel_count = 0
    consonant_count = 0
    
    for ch in s:
        if ch.isalpha():   
            if ch in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
    
    print(f"Vowels = {vowel_count}, Consonants = {consonant_count}")
print("Case 1:")
count_vowels_consonants("hello world")

print("\nCase 2:")
count_vowels_consonants("Python")
