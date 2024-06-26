price_oranges_premise = 50
price_oranges_hypothesis = 40

# the hypothesis talks about the average price of the pieces of fruit that Mary keeps, which is also referenced in the premise
if price_oranges_hypothesis!= price_oranges_premise:
    # check if the average price in the hypothesis contradicts the average price reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
