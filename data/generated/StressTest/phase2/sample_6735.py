# Premise: Rohit and Rohan can complete a work in 12 days and 6 days respectively.
# Hypothesis: Rohit and Rohan can complete a work in less than 22 days and 6 days respectively.
# Golden Label: entailment

rohit_work_days_premise = 12
rohan_work_days_premise = 6
rohit_work_days_hypothesis = 22
rohan_work_days_hypothesis = 6

# the hypothesis refers to Rohit's and Rohan's work completion times mentioned in the premise
if rohit_work_days_hypothesis < rohit_work_days_premise or rohan_work_days_hypothesis != rohan_work_days_premise:
    # check if the hypothesis values contradict the work completion times in the premise
    label = "contradiction"
elif rohit_work_days_hypothesis > rohit_work_days_premise:
    # the hypothesis for Rohit's work completion time is more than the premise, but it can still be consistent with the premise
    # because it is less than the maximum possible work completion time
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

