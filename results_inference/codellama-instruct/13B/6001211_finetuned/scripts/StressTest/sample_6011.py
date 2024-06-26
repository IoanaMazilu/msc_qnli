race_gap_premise = 4
race_gap_hypothesis = 6
start_late_premise = 4
start_late_hypothesis = 4

# the hypothesis refers to the gap by which Karen will beat Tom and the delay of Karen's start, both mentioned in the premise
if race_gap_premise!= race_gap_hypothesis:
    # check if the gap by which Karen will beat Tom in the hypothesis contradicts the gap mentioned in the premise
    label = "contradiction"
elif start_late_premise!= start_late_hypothesis:
    # check if the delay of Karen's start in the hypothesis contradicts the delay mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
