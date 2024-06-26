pencils_josh_premise = 142.0
pencils_given_premise = 31.0
pencils_left_hypothesis = 106.0

# the hypothesis refers to the number of pencils Josh has left, which is also mentioned in the premise
# compute the number of pencils Josh has left in the premise
pencils_left_premise = pencils_josh_premise - pencils_given_premise
if pencils_left_hypothesis!= pencils_left_premise:
    # check if the number of pencils Josh has left in the hypothesis contradicts the number of pencils left in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
