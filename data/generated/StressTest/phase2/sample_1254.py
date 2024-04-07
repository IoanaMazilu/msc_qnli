# Premise: The distance from Steve's house to work is 30 Km.
# Hypothesis: The distance from Steve's house to work is more than 10 Km.
# Golden Label: entailment

distance_home_work_premise = 30
distance_home_work_hypothesis = 10

# the hypothesis refers to the distance from Steve's house to work, also mentioned in the premise
if distance_home_work_hypothesis > distance_home_work_premise:
    # check if the hypothesis value contradicts the distance from Steve's house to work reported in the premise
    label = "contradiction"
elif distance_home_work_hypothesis == distance_home_work_premise:
    # check if the exact distance in the hypothesis contradicts the exact distance reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

