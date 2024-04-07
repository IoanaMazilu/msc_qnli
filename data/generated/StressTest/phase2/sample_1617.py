# Premise: At present, the ratio between the ages of Arun and Deepak is 4:3.
# Hypothesis: At present, the ratio between the ages of Arun and Deepak is more than 2:3.
# Golden Label: entailment

arun_deepak_ratio_premise = 4 / 3
arun_deepak_ratio_hypothesis = 2 / 3

# the hypothesis refers to the ratio of ages of Arun and Deepak mentioned in the premise
if arun_deepak_ratio_hypothesis >= arun_deepak_ratio_premise:
    # check if the ratio in the hypothesis contradicts the ratio of ages in the premise
    label = "contradiction"
else:
    # if the hypothesis ratio does not contradict the premise ratio, we can infer entailment
    label = "entailment"

print(label)

