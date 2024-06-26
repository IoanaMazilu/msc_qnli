race_gap_premise = 4
race_gap_hypothesis = 6
late_start_premise = 4
late_start_hypothesis = 4

# the hypothesis refers to the gap by which Karen will beat Tom and the delay of Karen's start, both mentioned in the premise
if race_gap_hypothesis!= race_gap_premise:
    # check if the gap by which Karen will beat Tom in the hypothesis contradicts the gap reported in the premise
    label = "contradiction"
elif late_start_hypothesis!= late_start_premise:
    # check if the delay of Karen's start in the hypothesis contradicts the delay reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
