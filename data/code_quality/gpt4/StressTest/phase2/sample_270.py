arun_deepak_ratio_premise = 4/3
arun_deepak_ratio_hypothesis = 1/3

# the hypothesis refers to the age ratio of Arun and Deepak mentioned in the premise
if arun_deepak_ratio_premise <= arun_deepak_ratio_hypothesis:
    # checking if the age ratio in the hypothesis contradicts the age ratio in the premise
    label = "contradiction"
else:
    # if the hypothesis ratio does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
