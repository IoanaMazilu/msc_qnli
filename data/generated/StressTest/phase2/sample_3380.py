# Premise: One hour after Yolanda started walking from X to Y, a distance of 10 miles, Bob started walking along the same road from Y to X.
# Hypothesis: One hour after Yolanda started walking from X to Y, a distance of more than 10 miles, Bob started walking along the same road from Y to X.
# Golden Label: contradiction

distance_walked_premise = 10
distance_walked_hypothesis = 10

# the hypothesis talks about the distance walked, which is also mentioned in the premise
if distance_walked_hypothesis > distance_walked_premise:
    # check if the hypothesis value contradicts the exact distance mentioned in the premise
    label = "contradiction"
elif distance_walked_hypothesis < distance_walked_premise:
    # check if the hypothesis value contradicts the exact distance mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

