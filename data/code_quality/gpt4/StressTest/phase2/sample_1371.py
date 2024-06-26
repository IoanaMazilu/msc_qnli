work_hours_suresh_premise = 9
work_hours_suresh_hypothesis = 3

# The hypothesis refers to the number of work hours of Suresh mentioned in the premise
if work_hours_suresh_hypothesis >= work_hours_suresh_premise:
    # Check if the estimate of 'work_hours_suresh_hypothesis' contradicts the number of work hours in the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
