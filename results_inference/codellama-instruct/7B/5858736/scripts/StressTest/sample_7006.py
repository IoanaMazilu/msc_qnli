# the hypothesis talks about the total number of pets, referenced also in the premise
if pets_total_hypothesis <= pets_total_premise:
    # check if the hypothesis value contradicts the estimate of more than 'pets_total_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the total number of pets
    # any number of pets greater than 'pets_total_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
