# Premise: If Fred walks at a constant speed of 5 miles per hour and Sam walks at a constant speed of 5 miles per hour, how many miles has Sam walked when they meet?
# Hypothesis: If Fred walks at a constant speed of 8 miles per hour and Sam walks at a constant speed of 5 miles per hour, how many miles has Sam walked when they meet?
# Golden Label: contradiction

fred_speed_premise = 5
sam_speed_premise = 5
fred_speed_hypothesis = 8
sam_speed_hypothesis = 5

# the hypothesis talks about Fred's and Sam's speed, referenced also in the premise
if fred_speed_hypothesis != fred_speed_premise or sam_speed_hypothesis != sam_speed_premise:
    # check if the speed values in the hypothesis contradict the speed values mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

