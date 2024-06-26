tommy_balloons_premise = 60.0
mom_gave_balloons_premise = 34.0
total_balloons_hypothesis = 91.0

# the hypothesis refers to the total number of balloons Tommy has, which is also calculated in the premise
# compute the total number of balloons in the premise
total_balloons_premise = tommy_balloons_premise + mom_gave_balloons_premise
if total_balloons_hypothesis != total_balloons_premise:
    # check if the total number of balloons in the hypothesis contradicts the total number of balloons from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
