orders_per_hour_premise = 40
orders_per_hour_hypothesis = 40
shifts_premise = 4
shifts_hypothesis = 36

# the hypothesis talks about the number of shifts Jill worked, which is also referred to in the premise
if shifts_hypothesis <= shifts_premise:
    # check if the hypothesis value contradicts the estimate of'shifts_premise'
    label = "contradiction"
elif orders_per_hour_hypothesis!= orders_per_hour_premise:
    # check if the number of orders per hour in the hypothesis contradicts the number of orders per hour reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
