age_man_premise = 18
age_man_hypothesis = 18

# the premise and hypothesis refer to the same person and the same age
if age_man_premise!= age_man_hypothesis:
    # check if the age in the hypothesis contradicts the age in the premise
    label = "contradiction"
else:
    # the premise and hypothesis refer to the same person and the same age
    label = "entailment"

print(label)
