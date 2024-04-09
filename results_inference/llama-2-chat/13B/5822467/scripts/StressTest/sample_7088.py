dan_work_premise = 6
dan_work_hypothesis = 3
annie_work_premise = 6

# the hypothesis refers to the time it takes Annie to complete the job, given Dan's work
if dan_work_hypothesis < annie_work_premise:
    # check if the hypothesis value contradicts the estimate of Dan's work time in the premise
    label = "contradiction"
elif dan_work_premise!= annie_work_premise:
    # check if the hypothesis value contradicts the number of hours Annie needs to complete the job, reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
