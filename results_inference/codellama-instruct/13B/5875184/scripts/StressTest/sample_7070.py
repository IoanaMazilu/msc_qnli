premise = "If she worked two 8-hour shifts this week and averaged $40 in orders per hour, how much did Jill earn this week?"
hypothesis = "If she worked two more than 8-hour shifts this week and averaged $40 in orders per hour, how much did Jill earn this week?"

# extract the numerical entities from the premise
premise_hours = 8
premise_orders = 40

# extract the numerical entities from the hypothesis
hypothesis_hours = 8
hypothesis_orders = 40

# check if the hypothesis value contradicts the premise value
if hypothesis_hours < premise_hours:
    label = "contradiction"
elif hypothesis_orders < premise_orders:
    label = "contradiction"
else:
    label = "neutral"

print(label)
