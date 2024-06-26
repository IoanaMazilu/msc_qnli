marbles_premise = 16.0
marbles_lost = 7.0
marbles_hypothesis = 9.0

# the hypothesis talks about the number of marbles, which are also referenced in the premise
# find the total number of marbles in the premise 
total_marbles_premise = marbles_premise - marbles_lost
if total_marbles_hypothesis!= total_marbles_premise:
    # check if the total marbles from the hypothesis contradict the estimate of'marbles_premise'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"
    
print(label)
