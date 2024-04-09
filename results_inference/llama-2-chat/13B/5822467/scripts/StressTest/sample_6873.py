days_worked_premise = 60
days_worked_hypothesis = 40

# the hypothesis refers to the number of days worked, mentioned in the premise
if days_worked_premise <= days_worked_hypothesis:
    # check if the hypothesis value contradicts the estimate of 'days_worked_premise'
    label = "contradiction"
elif days_worked_hypothesis > days_worked_premise:
    # check if the hypothesis value entails the premise
    label = "entailment"
else:
    # the premise gives only an estimate for the number of days worked
    # any number of days worked greater than 'days_worked_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
