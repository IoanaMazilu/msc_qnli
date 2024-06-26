premise_price_drop = 28
hypothesis_price_drop = 28

# the hypothesis refers to the number of sold cookies and pies mentioned in the premise
if hypothesis_price_drop > premise_price_drop:
    # check if the estimate of 'hypothesis_price_drop' contradicts the number of cookie sales in the premise
    label = "contradiction"
elif hypothesis_price_drop == premise_price_drop:
    # check if the number of sold pies in the hypothesis contradicts the number of sold pies reported in the premise
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "neutral"

print(label)
