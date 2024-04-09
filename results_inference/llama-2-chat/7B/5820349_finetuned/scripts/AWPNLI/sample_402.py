picked_pears_premise = 42.0
sold_pears_premise = 17.0
left_pears_hypothesis = 25.0

# the hypothesis refers to the number of pears left, which are also mentioned in the premise
# compute the number of pears left in the premise
left_pears_premise = picked_pears_premise - sold_pears_premise
if left_pears_hypothesis!= left_pears_premise:
    # check if the number of pears left in the hypothesis contradicts the number of pears left from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
