hours_worked_james_premise = 45
hours_worked_harry_premise = 45
hours_worked_james_hypothesis = 45
hours_worked_harry_hypothesis = 45

# the premise and hypothesis refer to the same number of hours worked by James and Harry
if hours_worked_james_premise!= hours_worked_james_hypothesis:
    # check if the number of hours worked by James in the premise contradicts the number of hours worked by James in the hypothesis
    label = "contradiction"
elif hours_worked_harry_premise!= hours_worked_harry_hypothesis:
    # check if the number of hours worked by Harry in the premise contradicts the number of hours worked by Harry in the hypothesis
    label = "contradiction"
else:
    # the premise and hypothesis refer to the same number of hours worked by James and Harry
    label = "entailment"

print(label)
