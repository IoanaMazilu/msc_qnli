pets_premise = 56
pets_hypothesis = 96

# the hypothesis refers to the total number of pets mentioned in the premise
if pets_hypothesis <= pets_premise:
    # check if the estimate of 'pets_hypothesis' contradicts the number of pets in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of pets
    # any number of pets greater than 'pets_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
