# Premise: Working independently, Tina can do a certain job in 12 hours.
# Hypothesis: Working independently, Tina can do a certain job in more than 12 hours.
# Golden Label: contradiction

work_hours_tina_premise = 12
work_hours_tina_hypothesis = 12

# the hypothesis refers to the number of hours Tina can work independently, also mentioned in the premise
if work_hours_tina_hypothesis < work_hours_tina_premise:
    # check if the hypothesis estimate contradicts the work hours mentioned in the premise
    label = "contradiction"
elif work_hours_tina_hypothesis == work_hours_tina_premise:
    # if the hypothesis value equals the premise one, we can infer entailment
    label = "entailment"
else:
    # the hypothesis gives an estimate for the number of work hours
    # any number of hours greater than 'work_hours_tina_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

