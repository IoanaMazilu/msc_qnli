premise_offer = 80
hypothesis_offer = 20
premise_price = 100
hypothesis_price = 100

# the hypothesis refers to the offer and price mentioned in the premise
if hypothesis_offer <= premise_offer:
    # check if the estimate of 'hypothesis_offer' contradicts the offer in the premise
    label = "contradiction"
elif hypothesis_price!= premise_price:
    # check if the price in the hypothesis contradicts the price reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
