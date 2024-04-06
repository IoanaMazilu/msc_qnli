# Premise: A restaurant made 9.0 hamburgers to serve during lunch and only 3.0 were actually served.
# Hypothesis: 6.0 hamburgers were left over from lunch.
# Golden Label: entailment

made_hamburgers_premise = 9.0
served_hamburgers_premise = 3.0
left_hamburgers_hypothesis = 6.0

# the hypothesis refers to the number of hamburgers left over, which can be calculated from the premise
# compute the number of hamburgers left over in the premise
left_hamburgers_premise = made_hamburgers_premise - served_hamburgers_premise
if left_hamburgers_hypothesis != left_hamburgers_premise:
    # check if the number of hamburgers left over in the hypothesis contradicts the number from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

