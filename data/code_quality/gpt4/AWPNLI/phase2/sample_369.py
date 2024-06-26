initial_balloons_premise = 9.0
popped_balloons_premise = 5.0
jessica_balloons_premise = 2.0
total_balloons_hypothesis = 9.0

# the hypothesis refers to the total number of blue balloons, which are also mentioned in the premise
# compute the current number of balloons in the premise
current_balloons_premise = initial_balloons_premise - popped_balloons_premise + jessica_balloons_premise
if total_balloons_hypothesis != current_balloons_premise:
    # check if the number of balloons in the hypothesis contradicts the number of balloons from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
