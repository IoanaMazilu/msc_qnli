pencils_premise = 142.0
given_pencils_premise = 31.0
left_pencils_hypothesis = 106.0

# the hypothesis refers to the number of pencils left, which can be computed from the premise
# compute the number of pencils left in the premise
left_pencils_premise = pencils_premise - given_pencils_premise
if left_pencils_hypothesis != left_pencils_premise:
    # check if the number of pencils left in the hypothesis contradicts the number of pencils left from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
