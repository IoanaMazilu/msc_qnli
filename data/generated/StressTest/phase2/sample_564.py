# Premise: Lionel left his house and walked towards Walt's house, 48 miles away.
# Hypothesis: Lionel left his house and walked towards Walt's house, more than 28 miles away.
# Golden Label: entailment

distance_premise = 48
distance_hypothesis = 28

# the hypothesis talks about the distance from Lionel's house to Walt's house, referenced also in the premise
if distance_premise < distance_hypothesis:
    # check if the distance in the premise contradicts the estimate of more than 'distance_hypothesis'
    label = "contradiction"
elif distance_hypothesis != distance_premise:
    # check if the distance in the hypothesis contradicts the distance reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

