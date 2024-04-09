orange_balloons_premise = 9.0
blue_balloons_premise = 4.0
more_orange_balloons_premise = 2.0
total_balloons_hypothesis = 13.0

# compute the total number of orange balloons in the premise
total_orange_balloons_premise = orange_balloons_premise + more_orange_balloons_premise

if total_balloons_hypothesis > total_orange_balloons_premise:
    # check if the number of orange balloons in the hypothesis contradicts the number of orange balloons from the premise
    label = "contradiction"
elif total_balloons_hypothesis < total_orange_balloons_premise:
    # check if the number of blue balloons in the hypothesis contradicts the number of blue balloons from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
