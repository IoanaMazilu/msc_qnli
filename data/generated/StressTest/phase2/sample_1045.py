# Premise: In the city of San Durango, more than 50 people own cats, dogs, or rabbits.
# Hypothesis: In the city of San Durango, 60 people own cats, dogs, or rabbits.
# Golden Label: neutral

pet_owners_premise = 50
pet_owners_hypothesis = 60

# the hypothesis talks about the number of pet owners in San Durango, referenced also in the premise
if pet_owners_hypothesis <= pet_owners_premise:
    # check if the hypothesis value contradicts the estimate of more than 'pet_owners_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of pet owners
    # any number of pet owners greater than 'pet_owners_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

