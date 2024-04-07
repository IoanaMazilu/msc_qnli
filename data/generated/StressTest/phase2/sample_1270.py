# Premise: In the city of San Durango, more than 60 people own cats, dogs, or rabbits.
# Hypothesis: In the city of San Durango, 90 people own cats, dogs, or rabbits.
# Golden Label: neutral

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

