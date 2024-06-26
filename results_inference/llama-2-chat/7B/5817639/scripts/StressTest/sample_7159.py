age_premise = 4
age_hypothesis = 6

# the hypothesis refers to Sandy's age in the future, based on the premise
if age_hypothesis <= age_premise:
    # check if the estimate of 'age_hypothesis' contradicts the current age of Sandy in the premise
    label = "contradiction"
else:
    # the premise gives an estimate for Sandy's age in the future, which is consistent with the hypothesis
    label = "entailment"

print(label)
