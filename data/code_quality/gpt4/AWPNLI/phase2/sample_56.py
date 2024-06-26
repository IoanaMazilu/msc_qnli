wheat_bread_premise = 0.5
white_bread_premise = 0.4
total_bread_hypothesis = 0.9

# the hypothesis refers to the total amount of bread, which is also mentioned in the premise
# compute the total amount of bread in the premise
total_bread_premise = wheat_bread_premise + white_bread_premise
if total_bread_hypothesis != total_bread_premise:
    # check if the total amount of bread in the hypothesis contradicts the total amount of bread from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
