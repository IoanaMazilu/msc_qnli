orders_premise = 40
orders_hypothesis = 40

# the hypothesis talks about the number of hours worked and the average orders per hour, both mentioned in the premise
if orders_hypothesis <= orders_premise:
    # check if the hypothesis value contradicts the estimate of 'orders_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of hours worked and the average orders per hour
    # any number of hours and average orders consistent with the premise is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
