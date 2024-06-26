fresh_fruit_premise = 9792.0 - 3513.0
fresh_fruit_hypothesis = 6279.0

# the hypothesis talks about the number of fresh fruit sold, which is also referenced in the premise
# compute the total number of fresh fruit sold from the premise
total_fresh_fruit_premise = fresh_fruit_premise
if fresh_fruit_hypothesis!= total_fresh_fruit_premise:
    # check if the number of fresh fruit from the hypothesis contradicts the number of fresh fruit from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"
    
print(label)
