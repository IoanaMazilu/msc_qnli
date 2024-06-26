aaron_jelly_beans_premise = 5
aaron_jelly_beans_hypothesis = 7
bianca_jelly_beans_premise = 7
bianca_jelly_beans_hypothesis = 7
callie_jelly_beans_premise = 8
callie_jelly_beans_hypothesis = 8
dante_jelly_beans_premise = 13
dante_jelly_beans_hypothesis = 13

# the hypothesis refers to the number of jelly beans each child has, as mentioned in the premise
if aaron_jelly_beans_premise >= aaron_jelly_beans_hypothesis:
    # check if the number of jelly beans Aaron has in the premise contradicts the estimate in the hypothesis
    label = "contradiction"
elif bianca_jelly_beans_premise!= bianca_jelly_beans_hypothesis:
    # check if the number of jelly beans Bianca has in the premise contradicts the number in the hypothesis
    label = "contradiction"
elif callie_jelly_beans_premise!= callie_jelly_beans_hypothesis:
    # check if the number of jelly beans Callie has in the premise contradicts the number in the hypothesis
    label = "contradiction"
elif dante_jelly_beans_premise!= dante_jelly_beans_hypothesis:
    # check if the number of jelly beans Dante has in the premise contradicts the number in the hypothesis
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
