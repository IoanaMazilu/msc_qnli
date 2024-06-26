jelly_beans_diff_premise = 1
jelly_beans_diff_hypothesis = 7

# the hypothesis refers to the difference in number of jelly beans between children, also mentioned in the premise
if jelly_beans_diff_hypothesis < jelly_beans_diff_premise:
    # check if the hypothesis value contradicts the estimate of 'jelly_beans_diff_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the difference in number of jelly beans
    # any difference greater than 'jelly_beans_diff_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
#