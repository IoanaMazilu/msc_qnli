pears_premise = 42.0
pears_sold_premise = 17.0
pears_left_hypothesis = 25.0

# the hypothesis refers to the number of pears left, which are also mentioned in the premise
# compute the total number of pears in the premise
total_pears_premise = pears_premise + pears_sold_premise
if pears_left_hypothesis!= total_pears_premise:
    # check if the number of pears in the hypothesis contradicts the number of pears from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
