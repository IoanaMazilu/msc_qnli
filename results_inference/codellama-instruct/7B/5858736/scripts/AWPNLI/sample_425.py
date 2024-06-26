bought_toys_premise = 1
marbles_price_premise = 9.05
football_price_premise = 4.95
returned_baseball_price_premise = 6.52

# the hypothesis refers to the net amount spent on toys, which is not mentioned in the premise
# compute the total amount spent on toys in the premise
total_toys_price_premise = marbles_price_premise + football_price_premise + returned_baseball_price_premise
if total_toys_price_premise!= 3.7:
    # check if the net amount spent on toys in the hypothesis contradicts the estimate of 3.7
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
