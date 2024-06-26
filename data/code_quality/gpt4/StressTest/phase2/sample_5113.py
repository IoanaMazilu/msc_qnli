animal_owners_premise = 70
animal_owners_hypothesis = 60

# the hypothesis talks about the number of people who own animals in San Durango, referenced also in the premise
if animal_owners_hypothesis >= animal_owners_premise:
    # check if the hypothesis value contradicts the estimate of less than 'animal_owners_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of people who own animals
    # any number of people less than 'animal_owners_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
