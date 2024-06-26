aaron_beans_premise = 7
aaron_beans_hypothesis = 5
bianca_beans_premise = 7
bianca_beans_hypothesis = 7
callie_beans_premise = 8
callie_beans_hypothesis = 8
dante_beans_premise = 13
dante_beans_hypothesis = 13

# the hypothesis talks about the number of jelly beans each child has, referenced also in the premise
if aaron_beans_hypothesis >= aaron_beans_premise:
    # check if the hypothesis value contradicts the estimate of less than 'aaron_beans_premise'
    label = "contradiction"
elif bianca_beans_hypothesis!= bianca_beans_premise:
    # check if the number of beans Bianca has in the hypothesis contradicts the number of beans Bianca has reported in the premise
    label = "contradiction"
elif callie_beans_hypothesis!= callie_beans_premise:
    # check if the number of beans Callie has in the hypothesis contradicts the number of beans Callie has reported in the premise
    label = "contradiction"
elif dante_beans_hypothesis!= dante_beans_premise:
    # check if the number of beans Dante has in the hypothesis contradicts the number of beans Dante has reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
