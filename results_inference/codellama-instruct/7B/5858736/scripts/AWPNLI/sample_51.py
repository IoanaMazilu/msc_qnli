premise_fresh_fruit = 9792.0
premise_frozen_fruit = 3513.0
premise_total_fruit = premise_fresh_fruit + premise_frozen_fruit
hypothesis_fresh_fruit = 6280.0

# the hypothesis refers to the number of fresh fruit sold, which is also mentioned in the premise
# compute the total number of fresh fruit sold in the premise
total_fresh_fruit_premise = premise_fresh_fruit
if total_fresh_fruit_hypothesis >= total_fresh_fruit_premise:
    # check if the total fresh fruit from the hypothesis contradicts the estimate of more than 'total_fresh_fruit_premise'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
