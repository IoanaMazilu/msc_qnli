premise = "If she worked four 16-hour shifts this week and averaged $40 in orders per hour, how much did Jill earn this week?"
hypothesis = "If she worked four more than 16-hour shifts this week and averaged $40 in orders per hour, how much did Jill earn this week?"

# extract the numerical entities from the premise
premise_shifts = 4
premise_hours = 16
premise_orders = 40

# extract the numerical entities from the hypothesis
hypothesis_shifts = 4
hypothesis_hours = 16
hypothesis_orders = 40

# check if the hypothesis contradicts the premise
if hypothesis_shifts < premise_shifts:
    label = "contradiction"
elif hypothesis_hours < premise_hours:
    label = "contradiction"
elif hypothesis_orders < premise_orders:
    label = "contradiction"
else:
    label = "neutral"

print(label)
