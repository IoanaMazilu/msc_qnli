shift_premise = 4 * 8 = 32
order_premise = 40
hypothesis_shifts = 4 + 8
hypothesis_orders = 40

# the hypothesis talks about the number of shifts and orders, both mentioned in the premise
if hypothesis_shifts > shift_premise or hypothesis_orders!= order_premise:
    # check if the hypothesis values contradict the number of shifts or orders reported in the premise
    label = "contradiction"
elif hypothesis_shifts == shift_premise and hypothesis_orders == order_premise:
    # if the number of shifts and orders in the hypothesis match the premise, we can infer entailment
    label = "entailment"
else:
    # the premise gives only an estimate for Jill's earnings
    # any amount greater than or equal to the premise estimate is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
