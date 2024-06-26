shifts_premise = 16
shifts_hypothesis = 16
avg_orders_premise = 40
avg_orders_hypothesis = 40

# the hypothesis talks about the number of shifts and average orders, referenced also in the premise
if shifts_hypothesis <= shifts_premise:
    # check if the hypothesis value contradicts the estimate of more than'shifts_premise'
    label = "contradiction"
elif avg_orders_hypothesis!= avg_orders_premise:
    # check if the average orders in the hypothesis contradicts the average orders reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of shifts
    # any number of shifts greater than'shifts_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
