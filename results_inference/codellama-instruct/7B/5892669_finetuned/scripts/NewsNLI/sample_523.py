overweight_percentage_premise = 69.5
overweight_percentage_hypothesis = 70

# the hypothesis mentions the percentage of overweight or obese population, which is also referenced in the premise
if overweight_percentage_hypothesis!= overweight_percentage_premise:
    # check if the percentage of overweight or obese in the hypothesis contradicts the percentage reported in the premise
    label = "contradiction"
else:
    # if the hypothesis percentage does not contradict the premise percentage, we can infer entailment
    label = "entailment"

print(label)
