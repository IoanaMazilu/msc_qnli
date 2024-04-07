# Premise: than how many more employees should NHAI hire to finish it in time working 10 hours a day?
# Hypothesis: than how many more employees should NHAI hire to finish it in time working less than 70 hours a day?
# Golden Label: entailment

work_hours_premise = 10
work_hours_hypothesis = 70

# the hypothesis refers to the number of work hours per day mentioned in the premise
if work_hours_hypothesis >= work_hours_premise:
    # check if the 'work_hours_hypothesis' contradicts the number of work hours in the premise
    label = "contradiction"
else:
    # if the hypothesis does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)

