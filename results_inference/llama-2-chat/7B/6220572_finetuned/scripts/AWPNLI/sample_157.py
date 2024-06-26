balloons_premise = 47.0 + 13.0
balloons_hypothesis = 63.0

# the hypothesis talks about the number of balloons, which is also referenced in the premise
if balloons_hypothesis!= balloons_premise:
    # check if the number of balloons in the hypothesis contradicts the number of balloons from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
