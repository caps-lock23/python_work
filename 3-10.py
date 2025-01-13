programming_languages = ["python", "c", "javascript"]

programming_languages.append("c++")
programming_languages.append("go")
programming_languages.append("rust")
programming_languages.append("c#")
programming_languages.insert(0, "java")

del programming_languages[-1]
pop_lang = programming_languages.pop()
programming_languages.remove("c")

print(programming_languages)
print(pop_lang)

print(sorted(programming_languages))

print(programming_languages)

print(sorted(programming_languages, reverse=True))

print(programming_languages)

programming_languages.sort()

print(programming_languages)

print(len(programming_languages))