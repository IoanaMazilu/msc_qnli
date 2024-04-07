# Premise: If Fred walks at a constant speed of 5 miles per hour and Sam walks at a constant speed of 5 miles per hour, how many miles has Sam walked when they meet?
# Hypothesis: If Fred walks at a constant speed of more than 1 miles per hour and Sam walks at a constant speed of 5 miles per hour, how many miles has Sam walked when they meet?
# Golden Label: entailment

fred_speed_premise = 5
fred_speed_hypothesis = 1
sam_speed_premise = 5
sam_speed_hypothesis = 5

# the hypothesis refers to the speeds of Fred and Sam mentioned in the premise
if fred_speed_premise <= fred_speed_hypothesis:
    # check if the estimate of 'fred_speed_hypothesis' contradicts the speed of Fred in the premise
    label = "contradiction"
elif sam_speed_hypothesis != sam_speed_premise:
    # check if the speed of Sam in the hypothesis contradicts the speed of Sam reported in the premise
    label = "contradiction"
else:
    # if the hypothesis speeds and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

