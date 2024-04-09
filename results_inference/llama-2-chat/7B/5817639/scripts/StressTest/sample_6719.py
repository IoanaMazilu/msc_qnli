jelly_beans_premise = [5, 7, 8, 13]
jelly_beans_hypothesis = [2, 7, 8, 13]

# the hypothesis refers to the number of jelly beans owned by each child mentioned in the premise
for i in range(4):
    if jelly_beans_hypothesis[i] <= jelly_beans_premise[i]:
        # check if the hypothesis value contradicts the estimate of 'jelly_beans_premise[i]'
        label = "contradiction"
        break
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
