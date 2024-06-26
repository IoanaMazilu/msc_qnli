quantity_premise = 20
quantity_hypothesis = 20
price_premise = 0
price_hypothesis = 0

# the hypothesis refers to the number of items purchased and the price mentioned in the premise
if quantity_hypothesis <= quantity_premise:
    # check if the estimate of 'quantity_hypothesis' contradicts the number of items purchased in the premise
    label = "contradiction"
elif price_hypothesis!= price_premise:
    # check if the price in the hypothesis contradicts the price mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
