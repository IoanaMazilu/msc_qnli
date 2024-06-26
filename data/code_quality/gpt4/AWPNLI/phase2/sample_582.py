initial_pencils_premise = 142.0
received_pencils_premise = 31.0
total_pencils_hypothesis = 173.0

# the hypothesis refers to the total number of pencils, which are also mentioned in the premise
# compute the total number of pencils in the premise
total_pencils_premise = initial_pencils_premise + received_pencils_premise
if total_pencils_hypothesis != total_pencils_premise:
    # check if the number of pencils in the hypothesis contradicts the number of pencils from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
