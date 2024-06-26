apples_picked_premise = 20
apples_picked_hypothesis = 10
apples_target_premise = 500
apples_target_hypothesis = 500

# the hypothesis refers to the number of picked apples and the target, mentioned in the premise
if apples_picked_premise <= apples_picked_hypothesis:
    # check if the hypothesis value contradicts the exact number of apples picked in the premise
    label = "contradiction"
elif apples_target_hypothesis != apples_target_premise:
    # check if the target number of apples in the hypothesis contradicts the target number of apples reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
