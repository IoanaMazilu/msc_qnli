# Premise: Kim can do a work in 3 days while David can do the same work in 2 days.
# Hypothesis: Kim can do a work in more than 1 days while David can do the same work in 2 days.
# Golden Label: entailment

kim_work_days_premise = 3
david_work_days_premise = 2
kim_work_days_hypothesis = 1
david_work_days_hypothesis = 2

# the hypothesis refers to the time Kim and David can finish a work, which is also mentioned in the premise
if kim_work_days_premise <= kim_work_days_hypothesis:
    # check if the estimate of 'kim_work_days_hypothesis' contradicts the number of work days for Kim in the premise
    label = "contradiction"
elif david_work_days_hypothesis != david_work_days_premise:
    # check if the number of work days for David in the hypothesis contradicts the number of work days for David reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

