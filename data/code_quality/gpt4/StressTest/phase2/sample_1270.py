pets_owners_premise = 60
pets_owners_hypothesis = 90

# the hypothesis refers to the number of people owning pets in the city of San Durango, as stated in the premise
if pets_owners_hypothesis <= pets_owners_premise:
    # check if the number of pet owners in the hypothesis contradicts the estimate of more than 'pets_owners_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of pet owners
    # any number of pet owners greater than 'pets_owners_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
