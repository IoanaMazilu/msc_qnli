# Premise: At present, the ratio between the ages of Arun and Deepak is 4:3.
# Hypothesis: At present, the ratio between the ages of Arun and Deepak is more than 3:3.
# Golden Label: entailment

arun_deepak_ratio_premise = 4 / 3
arun_deepak_ratio_hypothesis = 3 / 3

# the hypothesis refers to the age ratio of Arun and Deepak mentioned in the premise
if arun_deepak_ratio_premise <= arun_deepak_ratio_hypothesis:
    # check if the age ratio of Arun and Deepak in the hypothesis contradicts the age ratio in the premise
    label = "contradiction"
else:
    # the age ratio of Arun and Deepak in the hypothesis is less than the age ratio in the premise
    # so it can be entailed from the premise
    label = "entailment"

print(label)

