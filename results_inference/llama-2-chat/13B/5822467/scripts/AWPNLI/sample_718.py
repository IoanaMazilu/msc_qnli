if people_hypothesis <= 3 * people_friday_premise:
    label = "entailment"
elif people_hypothesis > 3 * people_friday_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
