# Premise: Mary works in a restaurant a maximum of 80 hours.
# Hypothesis: Mary works in a restaurant a maximum of more than 60 hours.
# Golden Label: entailment

max_hours_worked_premise = 80
max_hours_worked_hypothesis = 60

# the hypothesis talks about the maximum hours of work in a restaurant, referenced also in the premise
if max_hours_worked_hypothesis >= max_hours_worked_premise:
    # check if the hypothesis value contradicts the estimate of maximum 'max_hours_worked_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the maximum hours of work
    # any maximum hours of work less than 'max_hours_worked_premise' is consistent with the premise and can be explicitly entailed from the premise
    label = "entailment"

print(label)

