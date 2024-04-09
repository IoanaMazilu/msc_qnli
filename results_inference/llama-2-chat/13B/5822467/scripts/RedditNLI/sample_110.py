premise_pending_sales = 1.5
hypothesis_pending_sales = 1.5

# the premise and hypothesis mention the percentage change in pending sales of homes
if premise_pending_sales!= hypothesis_pending_sales:
    # check if the percentage change in the hypothesis contradicts the percentage change in the premise
    label = "contradiction"
elif hypothesis_pending_sales < premise_pending_sales:
    # check if the estimated percentage change in the hypothesis contradicts the premise estimate
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentage change
    # any estimate of the percentage change in the hypothesis greater or equal to the premise is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
