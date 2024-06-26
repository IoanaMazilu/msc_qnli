premise_self_portraits = 200000
hypothesis_self_portraits = 200000

if hypothesis_self_portraits > premise_self_portraits:
    label = "entailment"
elif hypothesis_self_portraits < premise_self_portraits:
    label = "contradiction"
else:
    label = "neutral"

print(label)
