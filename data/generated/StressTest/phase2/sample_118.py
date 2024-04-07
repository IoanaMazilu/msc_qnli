# Premise: In the city of San Durango, more than 10 people own cats, dogs, or rabbits.
# Hypothesis: In the city of San Durango, 90 people own cats, dogs, or rabbits.
# Golden Label: neutral

pet_owners_premise = 10
pet_owners_hypothesis = 90

# the hypothesis refers to the number of pet owners in San Durango mentioned in the premise
if pet_owners_hypothesis <= pet_owners_premise:
    # check if the number of pet owners in the hypothesis contradicts the estimate of more than 'pet_owners_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of pet owners
    # any number of pet owners greater than 'pet_owners_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

