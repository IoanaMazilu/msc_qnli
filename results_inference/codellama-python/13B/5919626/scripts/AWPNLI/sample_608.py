geese_premise = 58.0
ducks_premise = 37.0
geese_hypothesis = 21.0

# the hypothesis talks about the number of geese and ducks, which are also referenced in the premise
# find the total number of geese in the premise 
total_geese_premise = geese_premise + ducks_premise
if geese_hypothesis >= total_geese_premise:
    # check if the total geese from the hypothesis contradict the estimate of more than 'ducks_premise'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"
    
print(label)
