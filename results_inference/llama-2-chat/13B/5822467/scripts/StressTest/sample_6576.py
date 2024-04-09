shirt_price_premise = 160
shirt_price_hypothesis = 560

# the hypothesis refers to the number of shirts bought and the price per shirt
if shirt_price_hypothesis <= shirt_price_premise:
    # check if the estimate of'shirt_price_hypothesis' contradicts the price per shirt in the premise
    label = "contradiction"
elif shirt_price_hypothesis > shirt_price_premise:
    # check if the number of shirts bought in the hypothesis contradicts the number of shirts bought in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
