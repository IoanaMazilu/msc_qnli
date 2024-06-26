paul_work_days_premise = 70
paul_work_days_hypothesis = 80
rose_work_days_premise = 120
rose_work_days_hypothesis = 120

# the hypothesis talks about the time Paul and Rose need to complete a piece of work, referenced also in the premise
if paul_work_days_hypothesis <= paul_work_days_premise or rose_work_days_hypothesis != rose_work_days_premise:
    # check if the hypothesis values contradict the estimates in the premise
    label = "contradiction"
elif paul_work_days_hypothesis > paul_work_days_premise and rose_work_days_hypothesis == rose_work_days_premise:
    # check if the hypothesis values are consistent with the premise and can be entailed from it
    label = "entailment"
else:
    # any other situation would mean that the hypothesis does not contradict the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
