aaron_jelly_beans_premise = 5
aaron_jelly_beans_hypothesis = 2
bianca_jelly_beans_premise = 7
bianca_jelly_beans_hypothesis = 7
callie_jelly_beans_premise = 8
callie_jelly_beans_hypothesis = 8
dante_jelly_beans_premise = 13
dante_jelly_beans_hypothesis = 13

# the hypothesis refers to the number of jelly beans each child has, as mentioned in the premise
if aaron_jelly_beans_premise!= aaron_jelly_beans_hypothesis:
    # check if the number of jelly beans for Aaron in the hypothesis contradicts the number of jelly beans reported in the premise
    label = "contradiction"
elif bianca_jelly_beans_hypothesis!= bianca_jelly_beans_premise:
    # check if the number of jelly beans for Bianca in the hypothesis contradicts the number of jelly beans reported in the premise
    label = "contradiction"
elif callie_jelly_beans_hypothesis!= callie_jelly_beans_premise:
    # check if the number of jelly beans for Callie in the hypothesis contradicts the number of jelly beans reported in the premise
    label = "contradiction"
elif dante_jelly_beans_hypothesis!= dante_jelly_beans_premise:
    # check if the number of jelly beans for Dante in the hypothesis contradicts the number of jelly beans reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
