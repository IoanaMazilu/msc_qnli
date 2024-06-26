total_pears_premise = 93
pears_keith_premise = 47
pears_mike_premise = 12
pears_left_hypothesis = 81

# the hypothesis refers to the number of pears left, which are also mentioned in the premise
# compute the total number of pears left in the premise
pears_left_premise = total_pears_premise - pears_keith_premise - pears_mike_premise
if pears_left_hypothesis!= pears_left_premise:
    # check if the number of pears left from the hypothesis contradicts the number of pears left from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
