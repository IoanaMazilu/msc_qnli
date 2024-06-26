work_time_premise = 20
work_time_hypothesis = 30

# the hypothesis refers to the time it takes Ram and Shyam to do a piece of work together, which is also mentioned in the premise
if work_time_hypothesis!= work_time_premise:
    # check if the time it takes in the hypothesis contradicts the time it takes in the premise
    label = "contradiction"
else:
    # if the time it takes in the hypothesis does not contradict the time it takes in the premise, we can infer entailment
    label = "entailment"

print(label)
