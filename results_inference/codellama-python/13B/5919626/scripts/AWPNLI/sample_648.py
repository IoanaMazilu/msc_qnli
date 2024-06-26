pounds_oranges_premise = 45.0
pounds_oranges_bag_premise = 23.0
bags_hypothesis = 1.95652173913

# the hypothesis talks about the number of bags of oranges, which are also referenced in the premise
# find the total number of oranges in the premise 
total_oranges_premise = pounds_oranges_premise / pounds_oranges_bag_premise
if total_oranges_hypothesis >= total_oranges_premise:
    # check if the total oranges from the hypothesis contradict the estimate of more than 'total_oranges_premise'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"
    
print(label)
