sanket_time_premise = 15
sanket_time_hypothesis = 85

# the hypothesis refers to the time it took for Sanket to finish the race, which is also mentioned in the premise
if sanket_time_hypothesis != sanket_time_premise:
    # check if the time it took for Sanket to finish the race in the hypothesis contradicts the time in the premise
    label = "contradiction"
else:
    # if the hypothesis time does not contradict the premise time, we can infer entailment
    label = "entailment"

print(label)
