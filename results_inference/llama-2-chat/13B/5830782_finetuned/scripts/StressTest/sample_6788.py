hours_worked_james_premise = 41
hours_worked_james_hypothesis = 31

# the hypothesis refers to the number of hours James worked last week, as stated in the premise
if hours_worked_james_hypothesis!= hours_worked_james_premise:
    # check if the number of hours James worked in the hypothesis contradicts the number of hours reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
