josh_pencils_premise = 142.0
dorothy_pencils_premise = 31.0
josh_pencils_hypothesis = 106.0

# the hypothesis refers to the number of pencils left, which are also mentioned in the premise
# compute the total number of pencils left in the premise
total_pencils_premise = josh_pencils_premise - dorothy_pencils_premise
if josh_pencils_hypothesis!= total_pencils_premise:
    # check if the number of pencils left in the hypothesis contradicts the number of pencils left from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
