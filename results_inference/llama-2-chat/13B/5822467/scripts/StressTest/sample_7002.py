premise_days = 5
hypothesis_days = 3

# the hypothesis refers to the number of days worked together
if hypothesis_days <= premise_days:
    # check if the hypothesis value contradicts the estimate of 'premise_days'
    label = "contradiction"
elif premise_days!= hypothesis_days:
    # check if the number of days worked together in the hypothesis contradicts the number of days worked together in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
