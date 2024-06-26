served_hamburgers_premise = 9.0 - 3.0
left_over_hamburgers_hypothesis = 6.0

if left_over_hamburgers_hypothesis!= served_hamburgers_premise:
    # check if the number of left over hamburgers from the hypothesis contradicts the number of served hamburgers from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
