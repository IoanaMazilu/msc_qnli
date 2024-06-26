jelly_beans_difference_premise = 1
jelly_beans_difference_hypothesis = 7

# the hypothesis refers to the difference in the number of jelly beans between children, also mentioned in the premise
if jelly_beans_difference_hypothesis < jelly_beans_difference_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif jelly_beans_difference_hypothesis > jelly_beans_difference_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
