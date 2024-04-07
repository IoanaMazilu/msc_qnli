# Premise: Lionel left his house and walked towards Walt's house, 48 miles away.
# Hypothesis: Lionel left his house and walked towards Walt's house, less than 68 miles away.
# Golden Label: entailment

distance_to_walt_house_premise = 48
distance_to_walt_house_hypothesis = 68

# the hypothesis refers to the distance to Walt's house mentioned in the premise
if distance_to_walt_house_premise > distance_to_walt_house_hypothesis:
    # check if the distance in the premise contradicts the estimate of 'less than distance_to_walt_house_hypothesis'
    label = "contradiction"
elif distance_to_walt_house_premise < distance_to_walt_house_hypothesis:
    # if the premise value is less than the hypothesis value, we can infer entailment
    label = "entailment"
else:
    # if the premise value is equal to the hypothesis value, we can infer neutrality
    label = "neutral"

print(label)

