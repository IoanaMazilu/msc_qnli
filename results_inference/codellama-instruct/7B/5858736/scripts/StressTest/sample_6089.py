matt_days_premise = 12
matt_days_hypothesis = 72
peter_days_premise = 10
peter_days_hypothesis = 10

# the hypothesis refers to the number of days worked by Matt and Peter
if matt_days_hypothesis <= matt_days_premise:
    # check if the estimate of'matt_days_hypothesis' contradicts the number of days worked by Matt in the premise
    label = "contradiction"
elif peter_days_hypothesis!= peter_days_premise:
    # check if the number of days worked by Peter in the hypothesis contradicts the number of days worked by Peter reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
