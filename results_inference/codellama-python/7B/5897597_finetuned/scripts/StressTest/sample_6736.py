work_completion_time_rohit_premise = 22
work_completion_time_rohit_hypothesis = 12
work_completion_time_rohan_premise = 6
work_completion_time_rohan_hypothesis = 6

# the hypothesis refers to the work completion time of Rohit and Rohan mentioned in the premise
if work_completion_time_rohit_hypothesis >= work_completion_time_rohit_premise:
    # check if the work completion time of Rohit in the hypothesis contradicts the estimate of less than 'work_completion_time_rohit_premise'
    label = "contradiction"
elif work_completion_time_rohan_hypothesis!= work_completion_time_rohan_premise:
    # check if the work completion time of Rohan in the hypothesis contradicts the exact time reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the work completion time of Rohit
    # any work completion time less than 'work_completion_time_rohit_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
