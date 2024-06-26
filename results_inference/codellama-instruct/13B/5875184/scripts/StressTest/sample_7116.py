premise_germs = 4.32 * 10 ** 6
hypothesis_germs = 4.32 * 10 ** 30

if hypothesis_germs < premise_germs:
    label = "contradiction"
else:
    label = "neutral"

print(label)
