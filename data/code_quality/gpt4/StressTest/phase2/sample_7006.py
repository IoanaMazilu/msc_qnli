total_pets_premise = 56
total_pets_hypothesis = 96

# the hypothesis refers to the number of pets Claire has, which is also mentioned in the premise
if total_pets_hypothesis <= total_pets_premise:
    # check if the total number of pets in the hypothesis contradicts the estimate of more than 'total_pets_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of pets
    # any number of pets greater than 'total_pets_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
