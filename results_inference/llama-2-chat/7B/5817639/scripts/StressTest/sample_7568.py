orders_per_hour_premise = 40
orders_per_hour_hypothesis = 40

# the hypothesis talks about the number of hours worked and the average orders per hour, which are also referenced in the premise
if orders_per_hour_hypothesis <= orders_per_hour_premise:
    # check if the hypothesis value contradicts the estimate of 'orders_per_hour_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of hours worked and the average orders per hour
    # any number of hours worked and average orders per hour consistent with the premise is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
