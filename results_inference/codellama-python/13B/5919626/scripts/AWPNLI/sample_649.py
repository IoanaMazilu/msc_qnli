pounds_oranges_premise = 45.0
pounds_oranges_bag = 23.0
bags = 1.4

# the hypothesis talks about the number of bags, which are also referenced in the premise
# find the total number of oranges in the premise 
total_oranges_premise = pounds_oranges_premise / pounds_oranges_bag
if bags > total_oranges_premise:
    # check if the number of bags from the hypothesis contradicts the estimate of more than 'total_oranges_premise'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"
    
print(label)
