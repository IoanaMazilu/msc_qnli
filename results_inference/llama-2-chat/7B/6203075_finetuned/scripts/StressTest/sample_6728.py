total_fruit_premise = 10
total_fruit_hypothesis = 20
average_price_premise = 56
average_price_hypothesis = 56

# the hypothesis refers to the total number of fruits and their average price, both mentioned in the premise
if total_fruit_hypothesis!= total_fruit_premise:
    # check if the total number of fruits in the hypothesis contradicts the total number of fruits reported in the premise
    label = "contradiction"
elif average_price_hypothesis!= average_price_premise:
    # check if the average price of fruits in the hypothesis contradicts the average price of fruits reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
