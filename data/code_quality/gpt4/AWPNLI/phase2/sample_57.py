wheat_bread_premise = 0.5
white_bread_premise = 0.4
total_bread_hypothesis = 1.2

# the hypothesis refers to the total number of loaves, which is also mentioned in the premise
# compute the total number of loaves in the premise
total_bread_premise = wheat_bread_premise + white_bread_premise
if total_bread_hypothesis != total_bread_premise:
    # check if the total number of loaves in the hypothesis contradicts the total number of loaves from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
