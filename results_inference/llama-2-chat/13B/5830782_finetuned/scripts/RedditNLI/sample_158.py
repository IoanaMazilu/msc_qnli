factors_premise = 5
factors_hypothesis = 5

# the hypothesis and premise mention the number of factors contributing to the U.S. economy being a world beater
if factors_hypothesis!= factors_premise:
    # check if the number of factors in the hypothesis contradicts the number of factors in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)