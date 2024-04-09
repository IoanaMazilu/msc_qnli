initial_pencils_premise = 142.0
given_pencils_premise = 31.0
remaining_pencils_hypothesis = 106.0

# the hypothesis refers to the number of pencils left, which is also mentioned in the premise
# compute the remaining number of pencils in the premise
remaining_pencils_premise = initial_pencils_premise - given_pencils_premise
if remaining_pencils_hypothesis!= remaining_pencils_premise:
    # check if the number of pencils left in the hypothesis contradicts the number of pencils left from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
