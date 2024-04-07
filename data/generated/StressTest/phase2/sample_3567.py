# Premise: In the city of San Durango, 80 people own cats, dogs, or rabbits.
# Hypothesis: In the city of San Durango, more than 40 people own cats, dogs, or rabbits.
# Golden Label: entailment

pets_owners_premise = 80
pets_owners_hypothesis = 40

# the hypothesis talks about the number of pet owners in San Durango, referenced also in the premise
if pets_owners_hypothesis >= pets_owners_premise:
    # check if the hypothesis value contradicts the exact number of 'pets_owners_premise'
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)

