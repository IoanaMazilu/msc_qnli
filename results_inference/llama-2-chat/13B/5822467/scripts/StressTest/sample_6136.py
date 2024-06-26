premise_hours = less_than_61
hypothesis_hours = 41

# the premise mentions the total number of hours worked by James
if premise_hours <= hypothesis_hours:
    # check if the estimate of 'hypothesis_hours' contradicts the number of hours worked by James in the premise
    label = "contradiction"
elif hypothesis_hours!= premise_hours:
    # check if the number of hours worked by Harry in the hypothesis contradicts the number of hours worked by James in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
