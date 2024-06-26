premise = "If she worked four 16-hour shifts this week and averaged $40 in orders per hour, how much did Jill earn this week?"
hypothesis = "If she worked four less than 36-hour shifts this week and averaged $40 in orders per hour, how much did Jill earn this week?"

# extract the numerical entities from the premise and hypothesis
premise_hours = 16
premise_orders = 40
hypothesis_hours = 36
hypothesis_orders = 40

# calculate the total hours worked in the premise
premise_total_hours = premise_hours * 4

# calculate the total hours worked in the hypothesis
hypothesis_total_hours = hypothesis_hours * 4

# calculate the total orders earned in the premise
premise_total_orders = premise_orders * premise_total_hours

# calculate the total orders earned in the hypothesis
hypothesis_total_orders = hypothesis_orders * hypothesis_total_hours

# compare the total orders earned in the premise and hypothesis
if premise_total_orders > hypothesis_total_orders:
    label = "entailment"
elif premise_total_orders < hypothesis_total_orders:
    label = "contradiction"
else:
    label = "neutral"

print(label)
