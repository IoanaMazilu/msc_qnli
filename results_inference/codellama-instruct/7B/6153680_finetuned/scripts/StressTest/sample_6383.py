x_premise = 40
x_hypothesis = 50

# the hypothesis refers to the number of hours James is paid per hour, which is also mentioned in the premise
if x_hypothesis!= x_premise:
    # check if the number of hours in the hypothesis contradicts the number of hours in the premise
    label = "contradiction"
else:
    # if the number of hours in the hypothesis does not contradict the number of hours in the premise, we can infer entailment
    label = "entailment"

print(label)
