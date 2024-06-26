commute_hours_premise = 20
commute_hours_hypothesis = 20

# the hypothesis mentions the average commute time in the U.S., which is also mentioned in the premise
if commute_hours_hypothesis!= commute_hours_premise:
    # check if the commute time in the hypothesis contradicts the commute time in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
