text = "Деякий текст з голосними"
print(text)
words = text.split()
word = 0
for i in range(len(words)):
    if len(words[word]) > len(words[i]):
        word = i
print("Найкоротше слово:", words[word])

golosni = "aеєиіїоуюя"
print("Кількість голосних в тексті:", sum([text.count(i) for i in golosni]))
