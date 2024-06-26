pets_total_premise = 96
pets_total_hypothesis = 56

# the hypothesis refers to the total number of pets Claire has, which is also mentioned in the premise
if pets_total_hypothesis > pets_total_premise:
    # check if the hypothesis value contradicts the number of pets in the premise
    label = "contradiction"
elif pets_total_hypothesis == pets_total_premise:
    # check if the hypothesis value is the same as the number of pets in the premise
    label = "entailment"
else:
    # if the hypothesis value is less than the number of pets in the premise, it is neutral
    label = "neutral"

print(label)
