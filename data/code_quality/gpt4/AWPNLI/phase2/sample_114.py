distance_premise = 6.0
speed_premise = 3.0
total_hours_hypothesis = 2.0

# the hypothesis refers to the time Charles travelled, which can be inferred from the premise
# compute the total time Charles travelled in the premise
total_hours_premise = distance_premise / speed_premise
if total_hours_hypothesis != total_hours_premise:
    # check if the total time in the hypothesis contradicts the time calculated from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
