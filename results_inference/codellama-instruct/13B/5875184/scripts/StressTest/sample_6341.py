premise = "If she worked four 8-hour shifts this week and averaged $40 in orders per hour, how much did Jill earn this week?"
hypothesis = "If she worked four more than 8-hour shifts this week and averaged $40 in orders per hour, how much did Jill earn this week?"

# extract the numerical entities from the premise
premise_hours = 4
premise_orders = 40

# extract the numerical entities from the hypothesis
hypothesis_hours = 4
hypothesis_orders = 40

# check if the hypothesis hours contradict the premise hours
if hypothesis_hours <= premise_hours:
    label = "contradiction"
else:
    # check if the hypothesis orders contradict the premise orders
    if hypothesis_orders!= premise_orders:
        label = "contradiction"
    else:
        label = "neutral"

print(label)
