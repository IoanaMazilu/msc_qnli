bottles_premise = 45.0
drunk_premise = 14.0
sister_drunk_premise = 8.0

# compute the number of bottles left in the premise
left_bottles_premise = bottles_premise - (drunk_premise + sister_drunk_premise)

bottles_hypothesis = 18.0

# check if the number of bottles in the hypothesis contradicts the number of bottles left in the premise
if bottles_hypothesis > left_bottles_premise:
    label = "contradiction"
elif bottles_hypothesis < left_bottles_premise:
    label = "entailment"
else:
    label = "neutral"

print(label)
