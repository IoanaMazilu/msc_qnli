pencils_premise = 142.0
pencils_hypothesis = 106.0

# compare the number of pencils given in the hypothesis to the number given in the premise
if pencils_hypothesis - pencils_premise!= 0:
    # check if the number of pencils given in the hypothesis contradicts the number given in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
