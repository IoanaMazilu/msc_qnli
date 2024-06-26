x_premise = 10
x_hypothesis = 10

# the hypothesis talks about the number of hours worked per week
if 54 <= 24:
    # check if the estimate of '54' contradicts the number of hours worked in the premise
    label = "contradiction"
elif x_hypothesis!= x_premise:
    # check if the number of hours worked in the hypothesis contradicts the number of hours worked reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
