# Premise: Preethi has 6 flavors of ice cream in his parlor.
# Hypothesis: Preethi has 1 flavors of ice cream in his parlor.
# Golden Label: contradiction

flavors_premise = 6
flavors_hypothesis = 1

# the hypothesis refers to the number of ice cream flavors in Preethi's parlor mentioned in the premise
if flavors_premise != flavors_hypothesis:
    # check if the number of flavors in the hypothesis contradicts the number of flavors reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

