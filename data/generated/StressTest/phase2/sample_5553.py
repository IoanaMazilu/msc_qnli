# Premise: Six years ago, the ratio of ages of Kunal and Sagar was 6:5.
# Hypothesis: Six years ago, the ratio of ages of Kunal and Sagar was more than 1:5.
# Golden Label: entailment

kunal_sagar_ratio_premise = 6/5
kunal_sagar_ratio_hypothesis = 1/5

# the hypothesis refers to the ratio of ages of Kunal and Sagar six years ago, mentioned in the premise
if kunal_sagar_ratio_premise <= kunal_sagar_ratio_hypothesis:
    # check if the 'kunal_sagar_ratio_hypothesis' contradicts the ratio in the premise
    label = "contradiction"
else:
    # if the hypothesis ratio does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

