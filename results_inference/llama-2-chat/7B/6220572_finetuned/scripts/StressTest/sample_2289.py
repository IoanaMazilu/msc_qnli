jelly_beans_premise = 1
jelly_beans_hypothesis = 7

# the hypothesis refers to the number of jelly beans in the premise
if jelly_beans_hypothesis <= jelly_beans_premise:
    # check if the hypothesis value contradicts the estimate of more than 'jelly_beans_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of jelly beans
    # any number of jelly beans greater than 'jelly_beans_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
