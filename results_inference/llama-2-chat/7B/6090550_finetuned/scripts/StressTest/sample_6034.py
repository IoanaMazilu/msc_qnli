y = 40
people_owned_pets_premise = 70
people_owned_pets_hypothesis = 40

# the hypothesis talks about the number of people who own cats, dogs, or rabbits in San Durango, which is also referenced in the premise
if people_owned_pets_hypothesis >= people_owned_pets_premise:
    # check if the number of people owning pets in the hypothesis contradicts the premise statement of less than 'people_owned_pets_premise'
    label = "contradiction"
else:
    # the hypothesis value is less than the premise value, thus it does not contradict the premise
    # but since the hypothesis value is not explicitly entailed from the premise, we cannot infer entailment either
    label = "neutral"

print(label)



