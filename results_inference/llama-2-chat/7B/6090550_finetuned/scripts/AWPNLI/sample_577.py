balloons_tommy_premise = 60.0
balloons_mom_premise = 34.0
balloons_tommy_hypothesis = 91.0

# the hypothesis refers to the number of balloons Tommy has, which is also mentioned in the premise
# compute the total number of balloons Tommy has in the premise
total_balloons_tommy_premise = balloons_tommy_premise + balloons_mom_premise
if total_balloons_tommy_premise!= balloons_tommy_hypothesis:
    # check if the number of balloons in the hypothesis contradicts the number of balloons from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
