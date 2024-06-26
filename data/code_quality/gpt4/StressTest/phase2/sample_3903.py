total_fruits_premise = 10
total_fruits_hypothesis = 80
average_price_premise = 54
average_price_hypothesis = 54

# the hypothesis refers to the number of selected fruits and their average price mentioned in the premise
if total_fruits_hypothesis < total_fruits_premise:
    # check if the estimate of 'total_fruits_hypothesis' contradicts the number of fruits in the premise
    label = "contradiction"
elif average_price_hypothesis != average_price_premise:
    # check if the average price in the hypothesis contradicts the average price reported in the premise
    label = "contradiction"
elif total_fruits_hypothesis == total_fruits_premise and average_price_hypothesis == average_price_premise:
    # if the hypothesis values and estimates are exactly the same as the premise ones, we can infer entailment
    label = "entailment"
else:
    # if the total fruits in the hypothesis is more than the premise but average price is same, we infer neutral
    label = "neutral"

print(label)
