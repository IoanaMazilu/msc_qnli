items_purchased_premise = 20
items_purchased_hypothesis = 20

# the hypothesis refers to the number of items purchased from Ram by Mohan, also mentioned in the premise
if items_purchased_hypothesis > items_purchased_premise:
    # check if the number of items in the hypothesis contradicts the number of items reported in the premise
    label = "contradiction"
elif items_purchased_hypothesis == items_purchased_premise:
    # if the number of items in the hypothesis exactly matches with the premise, we can infer entailment
    label = "entailment"
else:
    # any other scenario would be considered as neutral
    label = "neutral"

print(label)
