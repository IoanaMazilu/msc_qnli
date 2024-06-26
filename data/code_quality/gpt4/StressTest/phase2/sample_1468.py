pets_premise = 76
pets_hypothesis = 86

# the hypothesis talks about the total number of pets, which is also referenced in the premise
if pets_hypothesis <= pets_premise:
    # check if the hypothesis value contradicts the estimate of more than 'pets_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the total number of pets
    # any total number of pets greater than 'pets_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
