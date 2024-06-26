max_hours_worked_premise = 15
max_hours_worked_hypothesis = 45

# the hypothesis talks about the maximum number of hours Mary can work, referenced also in the premise
if max_hours_worked_hypothesis <= max_hours_worked_premise:
    # check if the hypothesis value contradicts the premise which states more than 'max_hours_worked_premise'
    label = "contradiction"
else:
    # the premise gives an estimate for the maximum number of hours Mary can work
    # any number of hours greater than 'max_hours_worked_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
