premise_t_shirts_returned = 5
hypothesis_t_shirts_returned = 4
premise_average_price = 100
hypothesis_average_price = 100

# the hypothesis refers to the number of t-shirts returned and the average price of the remaining t-shirts
if hypothesis_t_shirts_returned < premise_t_shirts_returned:
    # check if the hypothesis value contradicts the number of t-shirts returned in the premise
    label = "contradiction"
elif hypothesis_average_price!= premise_average_price:
    # check if the hypothesis value contradicts the average price of the remaining t-shirts in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
