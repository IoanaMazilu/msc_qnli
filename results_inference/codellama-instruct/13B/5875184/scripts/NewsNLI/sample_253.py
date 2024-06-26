premise_chance = 500
hypothesis_chance = 5

if hypothesis_chance > premise_chance:
    label = "entailment"
elif hypothesis_chance < premise_chance:
    label = "contradiction"
else:
    label = "neutral"

print(label)
