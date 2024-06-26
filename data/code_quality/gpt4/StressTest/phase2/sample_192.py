kim_work_time_premise = 3
david_work_time_premise = 2
kim_work_time_hypothesis = 8
david_work_time_hypothesis = 2

# the hypothesis talks about the time Kim and David can complete a work, referenced also in the premise
if kim_work_time_hypothesis < kim_work_time_premise:
    # check if the time in hypothesis contradicts the time Kim can complete the work in the premise
    label = "contradiction"
elif david_work_time_hypothesis != david_work_time_premise:
    # check if the time in hypothesis contradicts the time David can complete the work in the premise
    label = "contradiction"
else:
    # if the times in hypothesis do not contradict the times in the premise, we can infer entailment
    label = "entailment"

print(label)
