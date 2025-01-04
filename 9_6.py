def all_variants(text):
    i = 0
    n = len(text) + 1
    while i != n:
        for j in range(i):
            yield text[j:i]
        i += 1



a = all_variants("abc")
for i in a:
    print(i)

# a
# b
# c
# ab
# bc
# abc