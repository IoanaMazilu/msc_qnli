work_completion_time_rohit_premise = 12
work_completion_time_rohit_hypothesis = 62
work_completion_time_rohan_premise = 6
work_completion_time_rohan_hypothesis = 6

# the hypothesis refers to the work completion time of Rohit and Rohan mentioned in the premise
if work_completion_time_rohit_premise!= work_completion_time_rohit_hypothesis:
    # check if the work completion time of Rohit in the hypothesis contradicts the work completion time of Rohit reported in the premise
    label = "contradiction"
elif work_completion_time_rohan_premise!= work_completion_time_rohan_hypothesis:
    # check if the work completion time of Rohan in the hypothesis contradicts the work completion time of Rohan reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
