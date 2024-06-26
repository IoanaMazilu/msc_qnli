money_given_premise = 95
money_given_hypothesis = 85

if money_given_premise <= money_given_hypothesis:
    label = "contradiction"
else:
    label = "neutral"

print(label)
