owner_additions_premise = 900
owner_additions_hypothesis = 800
price_premise = 1500

# the hypothesis refers to the size of the property and the price mentioned in the premise
if owner_additions_hypothesis > owner_additions_premise:
    # check if the estimate of 'owner_additions_hypothesis' contradicts the size of the property in the premise
    label = "contradiction"
elif price_premise!= price_hypothesis:
    # check if the price mentioned in the hypothesis contradicts the price reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
