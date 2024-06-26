y_premise = 96
y_hypothesis = 66

# the hypothesis talks about the total number of pets Claire has, which is also mentioned in the premise
if y_hypothesis!= y_premise:
    # check if the total number of pets in the hypothesis contradicts the total number of pets mentioned in the premise
    label = "contradiction"
else:
    # if the total number of pets in the hypothesis does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
