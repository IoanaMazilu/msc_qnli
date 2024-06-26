total_pets_premise = 82
total_pets_hypothesis = 92

# the hypothesis talks about the total number of pets Claire has, which is also referenced in the premise
if total_pets_hypothesis <= total_pets_premise:
    # check if the hypothesis value contradicts the estimate of more than 'total_pets_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the total number of pets
    # any total number of pets greater than 'total_pets_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
