children_premise = 4.0
pencils_premise = 2.0
total_pencils_hypothesis = 8.0

# compare the number of pencils in the hypothesis with the number of pencils in the premise
if total_pencils_hypothesis >= pencils_premise:
    # check if the total number of pencils in the hypothesis contradicts the number of pencils in the premise
    label = "contradiction"
elif children_hypothesis!= children_premise:
    # check if the number of children in the hypothesis contradicts the number of children in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"
    
print(label)
