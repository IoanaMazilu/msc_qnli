grape_premise = 1 kg * 68 = 680
grape_hypothesis = 7 kg * 68 = 4660
mango_premise = 9 kg * 48 = 432
mango_hypothesis = 9 kg * 48 = 4320

# Check if the hypothesis values contradict the premise values
if grape_hypothesis < grape_premise or mango_hypothesis < mango_premise:
    label = "contradiction"
elif grape_hypothesis > grape_premise or mango_hypothesis > mango_premise:
    label = "entailment"
else:
    label = "neutral"

print(label)
