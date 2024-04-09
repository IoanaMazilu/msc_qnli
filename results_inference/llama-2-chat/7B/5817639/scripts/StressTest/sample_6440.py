worked_shifts_premise = 4
worked_shifts_hypothesis = 70
orders_per_hour_premise = 40
orders_per_hour_hypothesis = 40

# the hypothesis talks about the number of worked shifts and the orders per hour, both referenced in the premise
if worked_shifts_hypothesis <= worked_shifts_premise:
    # check if the hypothesis value contradicts the estimate of 'worked_shifts_premise'
    label = "contradiction"
elif orders_per_hour_hypothesis!= orders_per_hour_premise:
    # check if the number of orders per hour in the hypothesis contradicts the number of orders per hour reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
