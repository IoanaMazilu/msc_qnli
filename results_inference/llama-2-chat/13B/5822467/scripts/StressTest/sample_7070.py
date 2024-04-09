shift_premise = 8
hour_premise = 2
order_premise = 40

# define variables with representative names for the numerical entities in both inputs
shift_hypothesis = 10
hour_hypothesis = 3
order_hypothesis = 40

# extract all quantities as valid numbers (integers or floats)
shift_premise = int(shift_premise)
hour_premise = int(hour_premise)
order_premise = float(order_premise)
shift_hypothesis = int(shift_hypothesis)
hour_hypothesis = int(hour_hypothesis)
order_hypothesis = float(order_hypothesis)

# perform calculations if necessary
total_orders_premise = order_premise * hour_premise
total_orders_hypothesis = order_hypothesis * hour_hypothesis

# compare the variables
if shift_hypothesis > shift_premise:
    # the hypothesis refers to a greater number of shifts than the premise
    label = "contradiction"
elif hour_hypothesis!= hour_premise:
    # the number of hours in the hypothesis contradicts the number of hours in the premise
    label = "contradiction"
elif order_hypothesis!= order_premise:
    # the number of orders in the hypothesis contradicts the number of orders in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
