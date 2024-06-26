arun_deepak_ratio_premise = 5 / 4
arun_deepak_ratio_hypothesis = 1 / 4

# the hypothesis refers to the age ratio of Arun and Deepak mentioned in the premise
if arun_deepak_ratio_premise <= arun_deepak_ratio_hypothesis:
    # check if the age ratio in the hypothesis contradicts the age ratio in the premise
    label = "contradiction"
else:
    # if the age ratio in the hypothesis does not contradict the age ratio in the premise, we can infer entailment
    label = "entailment"

print(label)
