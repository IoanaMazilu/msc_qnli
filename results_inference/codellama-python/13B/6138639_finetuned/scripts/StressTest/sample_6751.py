pets_owners_premise = 70
pets_owners_hypothesis = 50

# the hypothesis talks about the number of people who own pets in a city, referenced also in the premise
if pets_owners_hypothesis >= pets_owners_premise:
    # check if the hypothesis value contradicts the estimate of less than 'pets_owners_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of people who own pets
    # any number of people less than 'pets_owners_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
