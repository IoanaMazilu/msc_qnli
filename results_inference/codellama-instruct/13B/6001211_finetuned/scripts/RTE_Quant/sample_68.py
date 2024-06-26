barbie_price_premise = 3
barbie_price_hypothesis = 3

# the hypothesis talks about the price of the first Barbie doll which is also mentioned in the premise
if barbie_price_hypothesis!= barbie_price_premise:
    # check if the price in the hypothesis contradicts the price in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
