cents_premise = 50.0
cost_pencil_premise = 5.0
pencils_hypothesis = 12.0

# the hypothesis refers to the number of pencils that can be bought, which is also related to the premise
# compute the maximum number of pencils that can be bought in the premise
max_pencils_premise = cents_premise / cost_pencil_premise
if pencils_hypothesis != max_pencils_premise:
    # check if the number of pencils in the hypothesis contradicts the number of pencils that can be bought from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
