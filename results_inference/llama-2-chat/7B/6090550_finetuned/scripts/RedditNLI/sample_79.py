costa_coffee_premise = 5.1
costa_coffee_hypothesis = 5.1

# the hypothesis mentions the price of Costa Coffee deal, which is also mentioned in the premise
if costa_coffee_hypothesis!= costa_coffee_premise:
    # check if the price in the hypothesis contradicts the price in the premise
    label = "contradiction"
else:
    # if the hypothesis price does not contradict the premise price, we can infer entailment
    label = "entailment"

print(label)
