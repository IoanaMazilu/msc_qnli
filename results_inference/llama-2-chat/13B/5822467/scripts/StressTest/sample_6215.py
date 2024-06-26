premise_employees = 10
hypothesis_employees = 70

# the hypothesis talks about the number of employees working per day, referenced also in the premise
if hypothesis_employees <= premise_employees:
    # check if the hypothesis value contradicts the estimate of 'premise_employees'
    label = "contradiction"
elif premise_employees!= hypothesis_employees:
    # check if the number of employees in the hypothesis contradicts the number of employees reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
