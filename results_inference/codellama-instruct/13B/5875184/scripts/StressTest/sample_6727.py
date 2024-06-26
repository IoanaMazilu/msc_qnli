premise_total_fruit = 20
hypothesis_total_fruit = 10
premise_mean_price = 56
hypothesis_mean_price = 56

# the hypothesis refers to the number of selected fruits and the mean price, both mentioned in the premise
if hypothesis_total_fruit <= premise_total_fruit:
    # check if the hypothesis value contradicts the estimate of less than 'premise_total_fruit'
    label = "contradiction"
elif hypothesis_mean_price!= premise_mean_price:
    # check if the hypothesis value contradicts the estimate of the mean price in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
