# Premise: Kim can do a work in 3 days while David can do the same work in 2 days.
# Hypothesis: Kim can do a work in 1 days while David can do the same work in 2 days.
# Golden Label: contradiction

kim_work_time_premise = 3
kim_work_time_hypothesis = 1
david_work_time_premise = 2
david_work_time_hypothesis = 2

# the hypothesis talks about the time Kim and David need to finish a work, also referenced in the premise
if kim_work_time_hypothesis > kim_work_time_premise:
    # check if the timeframe in which Kim can finish the work according to the hypothesis contradicts the timeframe mentioned in the premise
    label = "contradiction"
elif david_work_time_hypothesis != david_work_time_premise:
    # check if the timeframe in which David can finish the work according to the hypothesis contradicts the timeframe mentioned in the premise
    label = "contradiction"
else:
    # the hypothesis values and estimates do not contradict the premise ones, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

