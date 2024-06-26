gold_price_premise = 1500
gold_price_hypothesis = 1500

# the hypothesis and premise mention the price of gold
if gold_price_hypothesis!= gold_price_premise:
    # check if the price of gold in the hypothesis contradicts the price of gold in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
