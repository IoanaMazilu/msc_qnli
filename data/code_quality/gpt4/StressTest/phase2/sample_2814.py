employees_premise = 215
employees_hypothesis = 815

# the hypothesis talks about the number of employees in the same company mentioned in the premise
if employees_premise >= employees_hypothesis:
    # check if 'employees_premise' contradicts the hypothesis of less than 'employees_hypothesis'
    label = "contradiction"
else:
    # the premise gives an exact number of employees which is less than 'employees_hypothesis'
    # so, it does not contradict the hypothesis, but it cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
