balloons_premise = 60
balloons_gift_premise = 34
balloons_hypothesis = 91

# the hypothesis talks about the current number of balloons, which is also referenced in the premise
# compute the current number of balloons in the premise
current_balloons_premise = balloons_premise + balloons_gift_premise
if balloons_hypothesis!= current_balloons_premise:
    # check if the number of balloons in the hypothesis contradicts the number of balloons from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
