dan_work_premise = 3
dan_work_hypothesis = 4
annie_work_premise = None
annie_work_hypothesis = None

# the hypothesis talks about the number of hours Annie will take to complete the job, referenced also in the premise
if dan_work_hypothesis <= dan_work_premise:
    # check if the hypothesis value contradicts the estimate of Dan's work time
    label = "contradiction"
elif annie_work_hypothesis!= annie_work_premise:
    # check if the number of hours Annie will take to complete the job contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
