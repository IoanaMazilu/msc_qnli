# Premise: Six years ago, the ratio of ages of Kunal and Sagar was 6:5.
# Hypothesis: Six years ago, the ratio of ages of Kunal and Sagar was more than 5:5.
# Golden Label: entailment

kunal_sagar_ratio_premise = 6/5
kunal_sagar_ratio_hypothesis = 5/5

# the hypothesis speaks about the ratio of Kunal and Sagar ages six years ago, which is also mentioned in the premise
if kunal_sagar_ratio_hypothesis >= kunal_sagar_ratio_premise:
    # check if the hypothesis value contradicts the stated ratio of 'kunal_sagar_ratio_premise'
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

