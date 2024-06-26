james_hours_worked_premise = 41
harry_hours_worked_hypothesis = 11

# the hypothesis refers to the number of hours James worked last week, which is also mentioned in the premise
if james_hours_worked_premise < harry_hours_worked_hypothesis:
    # check if the number of hours James worked in the premise contradicts the hypothesis
    label = "contradiction"
else:
    # if the number of hours James worked in the premise is greater than the number of hours in the hypothesis, it is entailed by the hypothesis
    label = "entailment"

print(label)
