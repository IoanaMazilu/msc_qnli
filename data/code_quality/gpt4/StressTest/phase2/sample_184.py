jelly_beans_difference_premise = 4
jelly_beans_difference_hypothesis = 1

# the hypothesis talks about the difference in the number of jelly beans each child has, mentioned also in the premise
if jelly_beans_difference_hypothesis != jelly_beans_difference_premise:
    # check if the difference in the number of jelly beans in the hypothesis contradicts the number difference reported in the premise
    label = "contradiction"
else:
    # if the difference in jelly beans in the hypothesis matches the difference mentioned in the premise, we can infer entailment
    label = "entailment"

print(label)
