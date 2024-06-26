sandy_molly_ratio_premise = 4 / 3
sandy_molly_ratio_hypothesis = 1 / 3

# the hypothesis refers to the ratio of Sandy and Molly's ages mentioned in the premise
if sandy_molly_ratio_premise <= sandy_molly_ratio_hypothesis:
    # check if the estimate of 'sandy_molly_ratio_hypothesis' contradicts the ratio in the premise
    label = "contradiction"
else:
    # if the hypothesis ratio does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
