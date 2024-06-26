# define variables for each child's jelly bean number
aaron_beans_premise = 7
aaron_beans_hypothesis = 5
bianca_beans_premise = 7
bianca_beans_hypothesis = 7
callie_beans_premise = 8
callie_beans_hypothesis = 8
dante_beans_premise = 13
dante_beans_hypothesis = 13

# check if the hypothesis values contradict the premise ones
if aaron_beans_hypothesis >= aaron_beans_premise:
    label = "contradiction"
elif bianca_beans_hypothesis!= bianca_beans_premise:
    label = "contradiction"
elif callie_beans_hypothesis!= callie_beans_premise:
    label = "contradiction"
elif dante_beans_hypothesis!= dante_beans_premise:
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
