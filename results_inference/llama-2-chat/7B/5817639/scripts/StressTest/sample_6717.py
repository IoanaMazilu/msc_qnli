jelly_beans_premise = 4
jelly_beans_hypothesis = 4

# the hypothesis talks about the number of jelly beans held by different children, mentioned in the premise
if jelly_beans_hypothesis <= jelly_beans_premise:
    # check if the hypothesis value contradicts the estimate of 'jelly_beans_premise'
    label = "contradiction"
elif jelly_beans_hypothesis > jelly_beans_premise:
    # check if the hypothesis value entails the premise
    label = "entailment"
else:
    # the premise gives only an estimate for the number of jelly beans
    # any number of jelly beans greater than 'jelly_beans_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
