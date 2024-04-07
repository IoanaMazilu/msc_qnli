# Premise: If Fred walks at a constant speed of 4 miles per hour and Sam walks at a constant speed of 4 miles per hour, how many miles has Sam walked when they meet?
# Hypothesis: If Fred walks at a constant speed of 7 miles per hour and Sam walks at a constant speed of 4 miles per hour, how many miles has Sam walked when they meet?
# Golden Label: contradiction

fred_speed_premise = 4
sam_speed_premise = 4
fred_speed_hypothesis = 7
sam_speed_hypothesis = 4

# the hypothesis refers to the speed of Fred and Sam mentioned in the premise
if fred_speed_premise != fred_speed_hypothesis or sam_speed_premise != sam_speed_hypothesis:
    # check if the speed of Fred or Sam in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the speed of Fred and Sam in the premise and hypothesis are the same, we can infer entailment
    label = "entailment"

print(label)

