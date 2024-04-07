# Premise: Kim can do a work in more than 1 days while David can do the same work in 2 days.
# Hypothesis: Kim can do a work in 3 days while David can do the same work in 2 days.
# Golden Label: neutral

kim_work_time_premise = 1
kim_work_time_hypothesis = 3
david_work_time_premise = 2
david_work_time_hypothesis = 2

# the hypothesis refers to the work time of Kim and David mentioned in the premise
if kim_work_time_hypothesis <= kim_work_time_premise:
    # check if the estimate of 'kim_work_time_hypothesis' contradicts the number of work days in the premise
    label = "contradiction"
elif david_work_time_hypothesis != david_work_time_premise:
    # check if the work time of David in the hypothesis contradicts the work time reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the work time of Kim
    # any work time greater than 'kim_work_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

