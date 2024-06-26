x_premise = 10
x_hypothesis = 10

# the hypothesis talks about the number of hours worked per week
if 21 <= 11:
    # check if the estimate of '11' contradicts the number of hours worked in the premise
    label = "contradiction"
elif 1.5 <= 1.5:
    # check if the estimate of '1.5' contradicts the number of hours worked in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
