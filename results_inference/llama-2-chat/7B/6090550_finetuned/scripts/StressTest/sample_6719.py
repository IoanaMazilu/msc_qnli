aaron_jelly_beans_premise = 5
bianca_jelly_beans_premise = 7
callie_jelly_beans_premise = 8
dante_jelly_beans_premise = 13

aaron_jelly_beans_hypothesis = 2
bianca_jelly_beans_hypothesis = 7
callie_jelly_beans_hypothesis = 8
dante_jelly_beans_hypothesis = 13

# the hypothesis refers to the number of jelly beans each child has, which is also mentioned in the premise
if aaron_jelly_beans_hypothesis!= aaron_jelly_beans_premise:
    # check if Aaron's jelly beans in the hypothesis contradicts the number of jelly beans reported in the premise
    label = "contradiction"
elif bianca_jelly_beans_hypothesis!= bianca_jelly_beans_premise:
    # check if Bianca's jelly beans in the hypothesis contradicts the number of jelly beans reported in the premise
    label = "contradiction"
elif callie_jelly_beans_hypothesis!= callie_jelly_beans_premise:
    # check if Callie's jelly beans in the hypothesis contradicts the number of jelly beans reported in the premise
    label = "contradiction"
elif dante_jelly_beans_hypothesis!= dante_jelly_beans_premise:
    # check if Dante's jelly beans in the hypothesis contradicts the number of jelly beans reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
