fruit_selection_premise = 20
fruit_selection_hypothesis = 10
average_price_premise = 56
average_price_hypothesis = 56

# the hypothesis refers to the number of selected fruits and their average price, also mentioned in the premise
if fruit_selection_hypothesis >= fruit_selection_premise:
    # check if the number of selected fruits in the hypothesis contradicts the premise's estimate of less than 'fruit_selection_premise'
    label = "contradiction"
elif average_price_hypothesis != average_price_premise:
    # check if the average price of fruits in the hypothesis contradicts the average price mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
