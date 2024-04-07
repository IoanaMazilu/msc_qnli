# Premise: In the city of San Durango, more than 40 people own cats, dogs, or rabbits.
# Hypothesis: In the city of San Durango, 80 people own cats, dogs, or rabbits.
# Golden Label: neutral

pet_owners_premise = 40
pet_owners_hypothesis = 80

# the hypothesis refers to the number of pet owners in San Durango, which is also mentioned in the premise
if pet_owners_premise >= pet_owners_hypothesis:
    # check if the number of pet owners in the hypothesis contradicts the premise estimate of more than 'pet_owners_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of pet owners
    # the number 'pet_owners_hypothesis' is consistent with the premise, but it cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

