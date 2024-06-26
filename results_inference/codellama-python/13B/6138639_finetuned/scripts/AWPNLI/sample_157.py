balloons_premise_1 = 47.0
balloons_premise_2 = 13.0
total_balloons_hypothesis = 63.0

# the hypothesis refers to the total number of balloons, which are also mentioned in the premise
# compute the total number of balloons in the premise
total_balloons_premise = balloons_premise_1 + balloons_premise_2
if total_balloons_hypothesis!= total_balloons_premise:
    # check if the total number of balloons in the hypothesis contradicts the total number of balloons from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
