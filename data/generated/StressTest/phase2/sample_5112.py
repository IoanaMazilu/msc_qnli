# Premise: In the city of San Durango, 60 people own cats, dogs, or rabbits.
# Hypothesis: In the city of San Durango, less than 70 people own cats, dogs, or rabbits.
# Golden Label: entailment

pet_owners_premise = 60
pet_owners_hypothesis = 70

# the hypothesis refers to the number of pet owners in the city of San Durango, mentioned in the premise
if pet_owners_premise > pet_owners_hypothesis:
    # check if the number of pet owners stated in the premise contradicts the estimate of less than 'pet_owners_hypothesis' in the hypothesis
    label = "contradiction"
elif pet_owners_premise < pet_owners_hypothesis:
    # if the number of pet owners stated in the premise is less than the estimate in the hypothesis, we can infer entailment
    label = "entailment"
else:
    # if the number of pet owners stated in the premise exactly matches the estimate in the hypothesis,
    # this is consistent with the hypothesis, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

