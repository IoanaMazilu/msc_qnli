purchase_premise = 2000
purchase_hypothesis = 7000

# the hypothesis refers to the amount of money Robert spent on US saving bonds, also mentioned in the premise
if purchase_hypothesis == purchase_premise:
    # check if the amount spent according to the hypothesis matches the one in the premise
    label = "entailment"
elif purchase_hypothesis > purchase_premise:
    # if the hypothesis value is greater than the amount spent according to the premise, it contradicts the premise
    label = "contradiction"
else:
    # any other situation would imply a neutral relation, as the premise does not provide more details
    label = "neutral"

print(label)
