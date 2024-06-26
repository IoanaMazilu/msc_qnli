balloons_premise = 47.0 + 13.0
hypothesis_balloons = 63.0

# check if the number of balloons in the hypothesis contradicts the number of balloons from the premise
if hypothesis_balloons!= balloons_premise:
    label = "contradiction"
elif hypothesis_balloons > balloons_premise:
    # check if the number of balloons in the hypothesis entails the estimate of more than 47 balloons
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
