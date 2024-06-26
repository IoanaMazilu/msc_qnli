driving_hours_premise = 8
driving_hours_hypothesis = 5

# the hypothesis talks about the number of driving hours from Town A to Town C, also mentioned in the premise
if driving_hours_hypothesis != driving_hours_premise:
    # check if the number of driving hours in the hypothesis contradicts the number of driving hours in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
