total_pencils_premise = 142.0
given_pencils_premise = 31.0
total_pencils_hypothesis = 106.0

# the hypothesis refers to the number of pencils, which are also mentioned in the premise
# compute the total number of pencils left in the premise
total_pencils_premise = total_pencils_premise - given_pencils_premise
if total_pencils_hypothesis!= total_pencils_premise:
    # check if the number of pencils in the hypothesis contradicts the number of pencils from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
