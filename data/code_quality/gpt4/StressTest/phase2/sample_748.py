pet_owners_premise = 40
pet_owners_hypothesis = 60

# the hypothesis mentions the number of pet owners in San Durango, which is also referenced in the premise
if pet_owners_hypothesis <= pet_owners_premise:
    # check if the hypothesis value contradicts the estimate of more than 'pet_owners_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of pet owners
    # any number of pet owners greater than 'pet_owners_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)