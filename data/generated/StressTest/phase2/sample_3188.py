# Premise: At present, the ratio between the ages of Arun and Deepak is 4:3.
# Hypothesis: At present, the ratio between the ages of Arun and Deepak is more than 4:3.
# Golden Label: contradiction

arun_deepak_ratio_premise = 4/3
arun_deepak_ratio_hypothesis = 4/3

# the hypothesis mentions the age ratio of Arun and Deepak, which is also referenced in the premise
if arun_deepak_ratio_hypothesis <= arun_deepak_ratio_premise:
    # check if the age ratio in the hypothesis contradicts the age ratio given in the premise
    label = "contradiction"
elif arun_deepak_ratio_hypothesis > arun_deepak_ratio_premise:
    # check if the age ratio in the hypothesis is more than the age ratio given in the premise
    label = "entailment"
else:
    # if the age ratios in the hypothesis and premise are equal, we can infer neutrality
    label = "neutral"

print(label)

