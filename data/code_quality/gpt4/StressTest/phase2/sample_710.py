paul_work_days_premise = 80
paul_work_days_hypothesis = 80
rose_work_days_premise = 120
rose_work_days_hypothesis = 120

# the hypothesis refers to the time Paul and Rose take to complete a piece of work, as stated in the premise
if paul_work_days_hypothesis < paul_work_days_premise:
    # check if the hypothesis value contradicts the time Paul needs to complete a piece of work as per the premise
    label = "contradiction"
elif rose_work_days_hypothesis != rose_work_days_premise:
    # check if the time Rose needs to complete a piece of work in the hypothesis contradicts the time stated in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
