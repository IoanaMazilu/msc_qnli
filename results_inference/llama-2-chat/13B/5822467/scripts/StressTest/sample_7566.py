shift_premise = 4 * 12 = 48
hourly_orders_premise = 40
hypothesis_shifts = 4 * (62 - 4) = 228
hourly_orders_hypothesis = 40

# the hypothesis refers to the number of shifts and hourly orders mentioned in the premise
if shift_premise <= hypothesis_shifts:
    # check if the estimate of 'hypothesis_shifts' contradicts the number of shifts in the premise
    label = "contradiction"
elif hourly_orders_premise!= hourly_orders_hypothesis:
    # check if the number of hourly orders in the hypothesis contradicts the number of hourly orders reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
