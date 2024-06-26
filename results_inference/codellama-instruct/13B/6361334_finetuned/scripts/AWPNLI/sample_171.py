pencils_premise = 142.0
pencils_given_premise = 31.0
pencils_hypothesis = 106.0

# the hypothesis refers to the number of pencils left, which are also mentioned in the premise
# compute the total number of pencils in the premise
total_pencils_premise = pencils_premise - pencils_given_premise
if pencils_hypothesis!= total_pencils_premise:
    # check if the number of pencils in the hypothesis contradicts the number of pencils from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
