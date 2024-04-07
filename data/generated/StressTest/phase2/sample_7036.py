# Premise: If Fred walks at a constant speed of less than 8 miles per hour and Sam walks at a constant speed of 5 miles per hour, how many miles has Sam walked when they meet?
# Hypothesis: If Fred walks at a constant speed of 5 miles per hour and Sam walks at a constant speed of 5 miles per hour, how many miles has Sam walked when they meet?
# Golden Label: neutral

fred_speed_premise = 8
fred_speed_hypothesis = 5
sam_speed_premise = 5
sam_speed_hypothesis = 5

# the hypothesis refers to the walking speeds of Fred and Sam mentioned in the premise
if fred_speed_hypothesis > fred_speed_premise:
    # check if Fred's walking speed in the hypothesis contradicts the maximum speed given in the premise
    label = "contradiction"
elif sam_speed_hypothesis != sam_speed_premise:
    # check if Sam's walking speed in the hypothesis contradicts Sam's walking speed in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

