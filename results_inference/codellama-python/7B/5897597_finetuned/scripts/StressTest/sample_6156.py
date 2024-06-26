sameer_anand_ratio_premise = 5/4
sameer_anand_ratio_hypothesis = 3/4

# the hypothesis refers to the ratio of Sameer's and Anand's ages mentioned in the premise
if sameer_anand_ratio_premise <= sameer_anand_ratio_hypothesis:
    # check if the ratio of'sameer_anand_ratio_hypothesis' contradicts the ratio of Sameer's and Anand's ages in the premise
    label = "contradiction"
else:
    # if the hypothesis ratio does not contradict the premise ratio, we can infer entailment
    label = "entailment"

print(label)
