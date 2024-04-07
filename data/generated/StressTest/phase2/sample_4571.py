# Premise: Six years ago, the ratio of ages of Kunal and Sagar was 6:5.
# Hypothesis: Six years ago, the ratio of ages of Kunal and Sagar was less than 6:5.
# Golden Label: contradiction

kunal_sagar_ratio_premise = 6 / 5
kunal_sagar_ratio_hypothesis = 6 / 5

# the hypothesis refers to the age ratio of Kunal and Sagar mentioned in the premise
if kunal_sagar_ratio_hypothesis >= kunal_sagar_ratio_premise:
    # check if the hypothesis contradicts the premise by stating the ratio was less than in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

