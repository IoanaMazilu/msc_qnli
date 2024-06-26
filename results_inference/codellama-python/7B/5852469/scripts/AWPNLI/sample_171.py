pencils_premise = 142.0
pencils_given_away = 31.0
pencils_hypothesis = 106.0

# the hypothesis refers to the number of pencils left after the transaction
# compute the number of pencils owned before the transaction
pencils_premise = pencils_premise - pencils_given_away
if pencils_hypothesis!= pencils_premise:
    # check if the number of pencils in the hypothesis contradicts the number of pencils from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
