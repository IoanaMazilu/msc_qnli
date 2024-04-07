# Premise: In the city of San Durango, 90 people own cats, dogs, or rabbits.
# Hypothesis: In the city of San Durango, more than 60 people own cats, dogs, or rabbits.
# Golden Label: entailment

pet_owners_premise = 90
pet_owners_hypothesis = 60

# the hypothesis refers to the number of pet owners in San Durango, also mentioned in the premise
if pet_owners_premise < pet_owners_hypothesis:
    # check if the number of pet owners in the premise contradicts the estimate of 'pet_owners_hypothesis'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

