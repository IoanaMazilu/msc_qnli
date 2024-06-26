jelly_beans_aaron_premise = 7
jelly_beans_aaron_hypothesis = 5
jelly_beans_bianca_premise = 7
jelly_beans_bianca_hypothesis = 7
jelly_beans_callie_premise = 8
jelly_beans_callie_hypothesis = 8
jelly_beans_dante_premise = 13
jelly_beans_dante_hypothesis = 13

# the hypothesis refers to the number of jelly beans each child has, which is also mentioned in the premise
if jelly_beans_aaron_hypothesis!= jelly_beans_aaron_premise:
    # check if the number of jelly beans in the hypothesis contradicts the number of jelly beans in the premise
    label = "contradiction"
elif jelly_beans_bianca_hypothesis!= jelly_beans_bianca_premise:
    # check if the number of jelly beans in the hypothesis contradicts the number of jelly beans in the premise
    label = "contradiction"
elif jelly_beans_callie_hypothesis!= jelly_beans_callie_premise:
    # check if the number of jelly beans in the hypothesis contradicts the number of jelly beans in the premise
    label = "contradiction"
elif jelly_beans_dante_hypothesis!= jelly_beans_dante_premise:
    # check if the number of jelly beans in the hypothesis contradicts the number of jelly beans in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
