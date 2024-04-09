premise_amount = 20000
premise_time = 6

hypothesis_amount = 20000
hypothesis_time = 7

# the premise refers to the amount invested for 6 months
if premise_amount <= hypothesis_amount:
    # check if the hypothesis value contradicts the estimate of the premise amount
    label = "contradiction"
elif hypothesis_time!= premise_time:
    # check if the time period in the hypothesis contradicts the time period in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
