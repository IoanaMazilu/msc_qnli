aaron_beans_premise = 8
aaron_beans_hypothesis = 5
bianca_beans_premise = 7
bianca_beans_hypothesis = 7
callie_beans_premise = 8
callie_beans_hypothesis = 8
dante_beans_premise = 19
dante_beans_hypothesis = 19

# the hypothesis talks about the number of jelly beans each child has, referenced also in the premise
if aaron_beans_hypothesis >= aaron_beans_premise:
    # check if the hypothesis value contradicts the premise of Aaron having less than 'aaron_beans_premise'
    label = "contradiction"
elif bianca_beans_hypothesis != bianca_beans_premise:
    # check if the number of jelly beans Bianca has in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
elif callie_beans_hypothesis != callie_beans_premise:
    # check if the number of jelly beans Callie has in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
elif dante_beans_hypothesis != dante_beans_premise:
    # check if the number of jelly beans Dante has in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
