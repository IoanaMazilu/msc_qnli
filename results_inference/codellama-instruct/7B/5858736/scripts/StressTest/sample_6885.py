currency_notes_premise = 85
currency_notes_hypothesis = 55

if currency_notes_hypothesis <= currency_notes_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
