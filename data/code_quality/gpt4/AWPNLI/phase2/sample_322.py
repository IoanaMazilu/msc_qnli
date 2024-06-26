nancy_balloons_premise = 7.0
mary_multiplier_premise = 4.0
mary_balloons_hypothesis = 28.0

# the hypothesis refers to the number of Mary's balloons, which are also calculated in the premise
# compute the number of Mary's balloons in the premise
mary_balloons_premise = nancy_balloons_premise * mary_multiplier_premise
if mary_balloons_hypothesis != mary_balloons_premise:
    # check if the number of Mary's balloons in the hypothesis contradicts the number of Mary's balloons from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
