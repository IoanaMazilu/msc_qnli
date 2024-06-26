balloons_blown_premise_1 = 47.0
balloons_blown_premise_2 = 13.0
total_balloons_premise = balloons_blown_premise_1 + balloons_blown_premise_2
balloons_hypothesis = 63.0

# the hypothesis refers to the number of balloons, which are also mentioned in the premise
# compute the total number of balloons in the premise
if total_balloons_premise!= balloons_hypothesis:
    # check if the number of balloons from the hypothesis contradicts the number of balloons from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"
    
print(label)
