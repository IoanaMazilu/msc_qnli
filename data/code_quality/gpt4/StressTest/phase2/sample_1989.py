aaron_beans_premise = 3
aaron_beans_hypothesis = 2
bianca_beans_premise = 7
bianca_beans_hypothesis = 7
callie_beans_premise = 8
callie_beans_hypothesis = 8
dante_beans_premise = 11
dante_beans_hypothesis = 11

# the hypothesis refers to the number of jelly beans each child has, as stated in the premise
if aaron_beans_premise <= aaron_beans_hypothesis:
    # check if the number of jelly beans Aaron has in the premise contradicts the estimate in the hypothesis
    label = "contradiction"
elif bianca_beans_premise != bianca_beans_hypothesis:
    # check if the number of jelly beans Bianca has in the premise contradicts the number in the hypothesis
    label = "contradiction"
elif callie_beans_premise != callie_beans_hypothesis:
    # check if the number of jelly beans Callie has in the premise contradicts the number in the hypothesis
    label = "contradiction"
elif dante_beans_premise != dante_beans_hypothesis:
    # check if the number of jelly beans Dante has in the premise contradicts the number in the hypothesis
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
