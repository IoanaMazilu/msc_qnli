# Premise: If Fred walks at a constant speed of 2 miles per hour and Sam walks at a constant speed of 5 miles per hour, how many miles has Sam walked when they meet?
# Hypothesis: If Fred walks at a constant speed of less than 7 miles per hour and Sam walks at a constant speed of 5 miles per hour, how many miles has Sam walked when they meet?
# Golden Label: entailment

fred_speed_premise = 2
sam_speed_premise = 5
fred_speed_hypothesis = 7
sam_speed_hypothesis = 5

# the hypothesis refers to the walking speeds of Fred and Sam, which are also mentioned in the premise
if fred_speed_premise >= fred_speed_hypothesis:
    # check if the estimate of 'fred_speed_premise' contradicts the maximum speed of Fred in the hypothesis
    label = "contradiction"
elif sam_speed_premise != sam_speed_hypothesis:
    # check if the speed of Sam in the hypothesis contradicts the speed of Sam reported in the premise
    label = "contradiction"
else:
    # if the speed values in the hypothesis do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

