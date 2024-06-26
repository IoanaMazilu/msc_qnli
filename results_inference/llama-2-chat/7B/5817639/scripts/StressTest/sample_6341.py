orders_per_hour_premise = 40
orders_per_hour_hypothesis = 40

# the hypothesis talks about the number of orders per hour, which is also mentioned in the premise
if orders_per_hour_hypothesis <= orders_per_hour_premise:
    # check if the hypothesis value contradicts the estimate of 'orders_per_hour_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of orders per hour
    # any number of orders per hour greater than 'orders_per_hour_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
