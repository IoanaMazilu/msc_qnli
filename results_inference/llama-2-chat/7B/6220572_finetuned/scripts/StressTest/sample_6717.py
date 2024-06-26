jelly_beans_premise = 4
jelly_beans_hypothesis = 4

# the hypothesis refers to the number of jelly beans each child has, as reported in the premise
if jelly_beans_hypothesis!= jelly_beans_premise:
    # check if the number of jelly beans in the hypothesis contradicts the number of jelly beans reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
