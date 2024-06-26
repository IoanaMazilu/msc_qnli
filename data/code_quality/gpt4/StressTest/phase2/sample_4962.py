working_hours_suresh_premise = 9
working_hours_suresh_hypothesis = 1

# the hypothesis refers to the working hours of Suresh mentioned in the premise
if working_hours_suresh_premise <= working_hours_suresh_hypothesis:
    # check if the estimate of 'working_hours_suresh_hypothesis' contradicts the number of working hours in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
