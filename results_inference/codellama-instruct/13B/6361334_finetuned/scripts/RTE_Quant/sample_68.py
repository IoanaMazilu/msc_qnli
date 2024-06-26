price_premise = 3
price_hypothesis = 3

# the hypothesis talks about the price of the first Barbie doll, which is also mentioned in the premise
if price_hypothesis!= price_premise:
    # check if the price in the hypothesis contradicts the price in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
