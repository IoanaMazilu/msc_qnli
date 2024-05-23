employees_premise = 218
employees_hypothesis = 118

# the hypothesis talks about the number of employees at Veridux Corporation, referenced also in the premise
if employees_hypothesis!= employees_premise:
    # check if the number of employees in the hypothesis contradicts the number of employees reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)