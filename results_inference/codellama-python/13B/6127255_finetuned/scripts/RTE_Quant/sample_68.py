first_barbie_price_premise = 3
first_barbie_price_hypothesis = 3

# the hypothesis talks about the price of the first Barbie doll, which is also mentioned in the premise
if first_barbie_price_hypothesis!= first_barbie_price_premise:
    # check if the price of the first Barbie doll in the hypothesis contradicts the price from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
