balloons_premise = 60.0
balloons_hypothesis = 91.0

# compare the number of balloons in the hypothesis to the number of balloons in the premise
if balloons_hypothesis > balloons_premise:
    # check if the number of balloons in the hypothesis contradicts the number of balloons in the premise
    label = "contradiction"
elif balloons_hypothesis - balloons_premise!= 0:
    # if the number of balloons in the hypothesis is less than the number of balloons in the premise, we can infer entailment
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer neutrality
    label = "neutral"

print(label)
