def caesar_cipher(word, shift):
    shift = -3
    abc_russ = "abcdefghijklmnopqrstuvwxyz"
    word_list = [abc_russ[(abc_russ.index(symbal) + shift) % 26] if symbal != " " else " " for symbal in " ".join(word)]
    print(word_list)
    shift = 1
    new_text = [abc_russ[(abc_russ.index(symbal) + shift) % 26] if symbal != " " else " " for symbal in " ".join(word_list)]
    return new_text
word_input = "vujgvmCfb tj ufscfu ouib z".lower().split()
print(word_input)
shift = 0
result = caesar_cipher(word_input, shift)

print("Зашифрованное сообщение:", " ".join(result))