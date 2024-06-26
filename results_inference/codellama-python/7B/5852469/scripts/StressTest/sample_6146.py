x_premise = 10
x_hypothesis = 10

# the hypothesis refers to the number of hours worked per week
if x_hypothesis <= x_premise:
    # check if the estimate of 'x_hypothesis' contradicts the number of hours worked in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of hours worked
    # any number of hours greater than 'x_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
