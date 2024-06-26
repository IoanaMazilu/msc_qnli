classes_premise = 2
classes_hypothesis = 3

# the hypothesis refers to the number of classes taught by Professor Wang mentioned in the premise
if classes_hypothesis <= classes_premise:
    # check if the number of classes in the hypothesis contradicts the estimate of more than 'classes_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of classes
    # any number of classes greater than 'classes_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
