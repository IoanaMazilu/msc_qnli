james_worked_premise = 45
james_worked_hypothesis = 35

# the hypothesis refers to the number of hours worked by James, also mentioned in the premise
if james_worked_hypothesis!= james_worked_premise:
    # check if the number of hours worked by James in the hypothesis contradicts the number of hours worked by James in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
