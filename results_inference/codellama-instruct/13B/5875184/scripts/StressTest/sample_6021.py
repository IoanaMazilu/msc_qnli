premise = 5000
hypothesis = 2000

if hypothesis > premise:
    label = "entailment"
elif hypothesis <= premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
