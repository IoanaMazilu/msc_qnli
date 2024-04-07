# Premise: In the city of San Durango, 50 people own cats, dogs, or rabbits.
# Hypothesis: In the city of San Durango, more than 50 people own cats, dogs, or rabbits.
# Golden Label: contradiction

pet_owners_premise = 50
pet_owners_hypothesis = 50

# the hypothesis refers to the estimated number of pet owners in San Durango
if pet_owners_hypothesis > pet_owners_premise:
    # check if the hypothesis estimate contradicts the exact number of pet owners in the premise
    label = "contradiction"
elif pet_owners_hypothesis == pet_owners_premise:
    # if the hypothesis value matches the premise, we can infer entailment
    label = "entailment"
else:
    # if the hypothesis value does not contradict the premise and it's not equal to it, then it must be neutral
    label = "neutral"

print(label)

