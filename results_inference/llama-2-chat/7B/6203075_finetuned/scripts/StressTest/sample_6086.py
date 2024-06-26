work_time_premise = 20
work_time_hypothesis = 30

# the hypothesis refers to the work time of Ram and Shyam mentioned in the premise
if work_time_hypothesis!= work_time_premise:
    # check if the work time in the hypothesis contradicts the work time reported in the premise
    label = "contradiction"
else:
    # if the work time in the hypothesis does not contradict the work time reported in the premise, we can infer entailment
    label = "entailment"

print(label)
