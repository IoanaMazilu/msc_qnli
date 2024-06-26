premise_fatalities = 4
hypothesis_fatalities = 5

if hypothesis_fatalities > premise_fatalities:
    label = "contradiction"
elif hypothesis_fatalities < premise_fatalities:
    label = "entailment"
else:
    label = "neutral"

print(label)
