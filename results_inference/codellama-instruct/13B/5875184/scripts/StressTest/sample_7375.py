premise_shifts = 4
premise_hours = 36
premise_orders = 40

hypothesis_shifts = 4
hypothesis_hours = 16
hypothesis_orders = 40

# check if the hypothesis values contradict the premise ones
if hypothesis_shifts!= premise_shifts:
    label = "contradiction"
elif hypothesis_hours!= premise_hours:
    label = "contradiction"
elif hypothesis_orders!= premise_orders:
    label = "contradiction"
else:
    label = "neutral"

print(label)
