# Premise: While driving from City A to City B, Bob drives at a constant speed of 40 miles per hour.
# Hypothesis: While driving from City A to City B, Bob drives at a constant speed of more than 40 miles per hour.
# Golden Label: contradiction

speed_premise = 40
speed_hypothesis = 40

# the hypothesis refers to the same speed of Bob while driving from City A to City B
if speed_hypothesis > speed_premise:
    # check if the speed in the hypothesis contradicts the speed mentioned in the premise
    label = "contradiction"
elif speed_hypothesis < speed_premise:
    # check if the speed in the hypothesis contradicts the speed mentioned in the premise
    label = "contradiction"
else:
    # if the speed in the hypothesis does not contradict the speed in the premise, we can infer entailment
    label = "entailment"

print(label)
