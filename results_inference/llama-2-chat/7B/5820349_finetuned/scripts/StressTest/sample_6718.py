aaron_beans_premise = 7
aaron_beans_hypothesis = 5
bianca_beans_premise = 7
bianca_beans_hypothesis = 7
callie_beans_premise = 8
callie_beans_hypothesis = 8
dante_beans_premise = 13
dante_beans_hypothesis = 13

# the hypothesis refers to the number of jelly beans each child has, as mentioned in the premise
if aaron_beans_hypothesis >= aaron_beans_premise:
    # check if the number of jelly beans Aaron has in the hypothesis contradicts the premise
    label = "contradiction"
elif bianca_beans_hypothesis!= bianca_beans_premise or callie_beans_hypothesis!= callie_beans_premise or dante_beans_hypothesis!= dante_beans_premise:
    # check if the number of jelly beans Bianca, Callie or Dante have in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
