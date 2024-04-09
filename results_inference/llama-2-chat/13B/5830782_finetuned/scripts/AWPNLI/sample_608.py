geese_premise = 58.0
ducks_premise = 37.0
more_geese_hypothesis = 21.0

# the hypothesis refers to the number of geese, which are also mentioned in the premise
# compute the difference in the number of geese and ducks in the premise
difference_premise = geese_premise - ducks_premise
if more_geese_hypothesis!= difference_premise:
    # check if the difference in the number of geese and ducks in the hypothesis contradicts the difference from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
