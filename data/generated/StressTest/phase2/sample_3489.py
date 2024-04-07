# Premise: At present, the ratio between the ages of Arun and Deepak is 4:5.
# Hypothesis: At present, the ratio between the ages of Arun and Deepak is less than 5:5.
# Golden Label: entailment

arun_deepak_ratio_premise = 4 / 5
arun_deepak_ratio_hypothesis = 5 / 5

# the hypothesis talks about the ratio between the ages of Arun and Deepak, referenced also in the premise
if arun_deepak_ratio_hypothesis <= arun_deepak_ratio_premise:
    # check if the hypothesis value contradicts the ratio value in the premise
    label = "contradiction"
else:
    # the ratio value in the hypothesis is larger than that in the premise, which does not contradict the premise
    # but it cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

