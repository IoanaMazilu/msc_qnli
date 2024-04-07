# Premise: A runner runs the 40 miles from Marathon to Athens at a constant speed.
# Hypothesis: A runner runs the more than 40 miles from Marathon to Athens at a constant speed.
# Golden Label: contradiction

distance_premise = 40
distance_hypothesis = 40

# the hypothesis refers to the distance run by a runner, which is also mentioned in the premise
if distance_hypothesis > distance_premise:
    # check if the estimate of 'distance_hypothesis' contradicts the distance in the premise
    label = "contradiction"
elif distance_hypothesis == distance_premise:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

