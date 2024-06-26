num_pets_premise = 70
num_pets_hypothesis = 50

# the hypothesis refers to the number of people owning cats, dogs, or rabbits in the city of San Durango
if num_pets_hypothesis >= num_pets_premise:
    # check if the hypothesis value contradicts the estimate of less than 'num_pets_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of people owning pets
    # any number of people owning pets less than 'num_pets_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
