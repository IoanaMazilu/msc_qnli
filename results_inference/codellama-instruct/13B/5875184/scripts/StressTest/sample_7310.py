premise_time = 8 / 4
hypothesis_time = 8 / 4

if hypothesis_time < premise_time:
    label = "entailment"
elif hypothesis_time == premise_time:
    label = "neutral"
else:
    label = "contradiction"

print(label)
