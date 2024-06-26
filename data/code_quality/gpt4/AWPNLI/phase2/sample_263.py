fans_premise = 2436.0
bleachers_premise = 3.0
fans_per_set_hypothesis = 814.0

# the hypothesis refers to the number of fans per set, which are also mentioned in the premise
# compute the number of fans per set in the premise
fans_per_set_premise = fans_premise / bleachers_premise
if fans_per_set_hypothesis != fans_per_set_premise:
    # check if the number of fans per set in the hypothesis contradicts the number of fans per set from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)