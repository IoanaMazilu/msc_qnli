premise_days_worked = 7
hypothesis_days_worked = 2
premise_joined_days = 14

# the hypothesis refers to the number of days worked and the number of days to complete the task mentioned in the premise
if hypothesis_days_worked <= premise_days_worked:
    # check if the estimate of 'hypothesis_days_worked' contradicts the number of days worked in the premise
    label = "contradiction"
elif premise_joined_days!= hypothesis_days_worked:
    # check if the number of days to complete the task in the hypothesis contradicts the number of days to complete the task reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
