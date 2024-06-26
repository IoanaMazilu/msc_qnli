premise_amount = 20000
premise_time = 7
hypothesis_amount = 20000
hypothesis_time = 6

# the hypothesis refers to the amount invested and the time period, both mentioned in the premise
if hypothesis_amount!= premise_amount:
    # check if the hypothesis value contradicts the amount invested in the premise
    label = "contradiction"
elif hypothesis_time!= premise_time:
    # check if the hypothesis value contradicts the time period in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
