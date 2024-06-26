geese_premise = 58.0
ducks_premise = 37.0
more_geese_hypothesis = 21.0

# the hypothesis talks about the difference between the number of geese and ducks, which are also referenced in the premise
# find the difference in the number of geese and ducks from the premise 
difference_premise = geese_premise - ducks_premise
if more_geese_hypothesis != difference_premise:
    # check if the difference from the hypothesis contradicts the difference from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"
    
print(label)
