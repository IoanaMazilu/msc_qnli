amount_premise = 95
amount_hypothesis = float(input("Enter the amount to give to John: "))

# check if the hypothesis value contradicts the premise value
if amount_premise!= amount_hypothesis:
    label = "contradiction"
elif amount_hypothesis < amount_premise:
    label = "entailment"
else:
    label = "neutral"

print(label)
