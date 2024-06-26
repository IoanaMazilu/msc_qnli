work_time_premise = 10
work_time_hypothesis = 20

# the hypothesis refers to the time it takes Ram and Shyam to finish a piece of work together, which is also mentioned in the premise
if work_time_hypothesis <= work_time_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
