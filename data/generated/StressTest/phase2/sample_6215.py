# Premise: than how many more emploies should NHAI hire to finish it in time working 10 hours a day.
# Hypothesis: than how many more emploies should NHAI hire to finish it in time working 70 hours a day.
# Golden Label: contradiction

working_hours_premise = 10
working_hours_hypothesis = 70

# the hypothesis and premise both talk about the number of working hours in a day
if working_hours_hypothesis != working_hours_premise:
    # check if the number of working hours in the hypothesis contradicts the number of working hours reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

