# Premise: than how many more emploies should NHAI hire to finish it in time working 10 hours a day.
# Hypothesis: than how many more emploies should NHAI hire to finish it in time working less than 80 hours a day.
# Golden Label: entailment

work_hours_premise = 10
work_hours_hypothesis = 80

# the hypothesis talks about working hours per day, which is also referenced in the premise
if work_hours_hypothesis < work_hours_premise:
    # check if the hypothesis value contradicts the working hours stated in the premise
    label = "contradiction"
elif work_hours_hypothesis > work_hours_premise:
    # the premise gives exact working hours per day
    # any working hours greater than 'work_hours_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the working hours in the hypothesis does not contradict the working hours in the premise, we can infer entailment
    label = "entailment"

print(label)

