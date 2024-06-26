balloons_premise = 60.0
balloons_given_premise = 34.0
balloons_hypothesis = 91.0

# the hypothesis refers to the total number of balloons, which are also mentioned in the premise
# compute the total number of balloons in the premise
total_balloons_premise = balloons_premise + balloons_given_premise
if total_balloons_hypothesis!= total_balloons_premise:
    # check if the number of balloons in the hypothesis contradicts the number of balloons from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
