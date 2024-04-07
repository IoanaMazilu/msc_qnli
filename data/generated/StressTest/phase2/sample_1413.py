# Premise: In the city of San Durango, 60 people own cats, dogs, or rabbits.
# Hypothesis: In the city of San Durango, less than 80 people own cats, dogs, or rabbits.
# Golden Label: entailment

pet_owners_premise = 60
pet_owners_hypothesis = 80

# the hypothesis talks about the number of pet owners in San Durango, referenced also in the premise
if pet_owners_hypothesis < pet_owners_premise:
    # check if the hypothesis value contradicts the number of pet owners reported in the premise
    label = "contradiction"
elif pet_owners_premise != pet_owners_hypothesis:
    # if the number of pet owners in the premise does not contradict the number of pet owners in the hypothesis
    # but also cannot be explicitly entailed from the premise, the relation is neutral
    label = "neutral"
else:
    # if the hypothesis value and estimate do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

