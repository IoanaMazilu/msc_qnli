aaron_jelly_beans_premise = 5
aaron_jelly_beans_hypothesis = 5
bianca_jelly_beans_premise = 7
bianca_jelly_beans_hypothesis = 7
callie_jelly_beans_premise = 8
callie_jelly_beans_hypothesis = 8
dante_jelly_beans_premise = 13
dante_jelly_beans_hypothesis = 13

# the hypothesis talks about the number of jelly beans each child has, which is also mentioned in the premise
if aaron_jelly_beans_hypothesis!= aaron_jelly_beans_premise:
    # check if Aaron's jelly beans in the hypothesis contradicts the number of jelly beans in the premise
    label = "contradiction"
elif Bianca_jelly_beans_hypothesis!= Bianca_jelly_beans_premise:
    # check if Bianca's jelly beans in the hypothesis contradicts the number of jelly beans in the premise
    label = "contradiction"
elif Callie_jelly_beans_hypothesis!= Callie_jelly_beans_premise:
    # check if Callie's jelly beans in the hypothesis contradicts the number of jelly beans in the premise
    label = "contradiction"
elif Dante_jelly_beans_hypothesis!= Dante_jelly_beans_premise:
    # check if Dante's jelly beans in the hypothesis contradicts the number of jelly beans in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
