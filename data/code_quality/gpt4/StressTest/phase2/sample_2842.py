work_duration_premise = 80
work_duration_hypothesis = 20
rajesh_duration_premise = 30
rajesh_duration_hypothesis = 30

# the hypothesis refers to the work durations mentioned in the premise
if work_duration_hypothesis >= work_duration_premise:
    # check if the work duration in the hypothesis contradicts the estimate of less than 'work_duration_premise'
    label = "contradiction"
elif rajesh_duration_hypothesis != rajesh_duration_premise:
    # check if the work duration of Rajesh in the hypothesis contradicts the work duration of Rajesh reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
