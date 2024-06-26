man_height_premise = 1.75
man_height_hypothesis = 1.75

# the premise and hypothesis refer to the same person and the same height
if man_height_premise!= man_height_hypothesis:
    # check if the height in the hypothesis contradicts the height in the premise
    label = "contradiction"
else:
    # the premise and hypothesis refer to the same person and the same height
    label = "entailment"

print(label)
