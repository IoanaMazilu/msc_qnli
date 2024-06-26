children_jelly_beans_premise = [5, 7, 8, 13]
children_jelly_beans_hypothesis = [5, 7, 8, 13]

# the hypothesis refers to the number of jelly beans for each child mentioned in the premise
if children_jelly_beans_hypothesis[0] > children_jelly_beans_premise[0]:
    # check if the estimate of 'children_jelly_beans_hypothesis[0]' contradicts the number of jelly beans for Aaron in the premise
    label = "contradiction"
elif children_jelly_beans_hypothesis[1]!= children_jelly_beans_premise[1]:
    # check if the number of jelly beans for Bianca in the hypothesis contradicts the number of jelly beans reported in the premise
    label = "contradiction"
elif children_jelly_beans_hypothesis[2]!= children_jelly_beans_premise[2]:
    # check if the number of jelly beans for Callie in the hypothesis contradicts the number of jelly beans reported in the premise
    label = "contradiction"
elif children_jelly_beans_hypothesis[3]!= children_jelly_beans_premise[3]:
    # check if the number of jelly beans for Dante in the hypothesis contradicts the number of jelly beans reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
