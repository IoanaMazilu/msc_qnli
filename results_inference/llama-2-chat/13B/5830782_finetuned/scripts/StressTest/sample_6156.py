sameer_anand_ratio_premise = 5 / 4
sameer_anand_ratio_hypothesis = 3 / 4

# the hypothesis refers to the ratio of ages of Sameer and Anand mentioned in the premise
if sameer_anand_ratio_premise <= sameer_anand_ratio_hypothesis:
    # check if the estimate of'sameer_anand_ratio_hypothesis' contradicts the ratio of ages in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)