fresh_fruit_sold_premise = 6279.0
frozen_fruit_sold_premise = 3513.0
total_fruit_sold_hypothesis = 9792.0

# the hypothesis refers to the number of pounds of fresh fruit sold, which is also mentioned in the premise
if fresh_fruit_sold_hypothesis!= fresh_fruit_sold_premise:
    # check if the number of pounds of fresh fruit sold from the hypothesis contradicts the number of pounds from the premise
    label = "contradiction"
elif frozen_fruit_sold_hypothesis!= frozen_fruit_sold_premise:
    # check if the number of pounds of frozen fruit sold from the hypothesis contradicts the number of pounds from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
