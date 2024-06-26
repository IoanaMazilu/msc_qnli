pears_picked_jason_premise = 46.0
pears_picked_keith_premise = 47.0
pears_eaten_mike_premise = 12.0
pears_left_hypothesis = 81.0

# the hypothesis refers to the number of pears left, which can be computed from the premise
# compute the total number of pears left in the premise
pears_left_premise = pears_picked_jason_premise + pears_picked_keith_premise - pears_eaten_mike_premise
if pears_left_hypothesis!= pears_left_premise:
    # check if the number of pears left in the hypothesis contradicts the number of pears left from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
