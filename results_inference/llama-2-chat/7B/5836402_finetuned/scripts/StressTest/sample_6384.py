james_worked_premise = 45
james_worked_hypothesis = 55

# the hypothesis refers to the number of hours worked by James mentioned in the premise
if james_worked_premise >= james_worked_hypothesis:
    # check if the estimate of 'james_worked_hypothesis' contradicts the number of hours worked by James in the premise
    label = "contradiction"
elif james_worked_premise < james_worked_hypothesis:
    # check if the number of hours worked by James in the premise is less than the estimate in the hypothesis
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer neutrality
    label = "neutral"

print(label)
