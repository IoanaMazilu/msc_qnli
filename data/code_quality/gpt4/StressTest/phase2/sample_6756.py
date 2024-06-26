time_premise = 8
time_hypothesis = 4

# the hypothesis refers to the time Tom goes, which is also mentioned in the premise
if time_hypothesis >= time_premise:
    # check if the time 'time_hypothesis' contradicts the time in the premise
    label = "contradiction"
else:
    # if the hypothesis time does not contradict the premise time, we can infer entailment
    label = "entailment"

print(label)
