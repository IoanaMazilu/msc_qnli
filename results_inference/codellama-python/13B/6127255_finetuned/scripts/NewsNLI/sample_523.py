overweight_obese_population_premise = 0.695
overweight_obese_population_hypothesis = 0.695

# the hypothesis mentions the percentage of the population overweight or obese, which is also mentioned in the premise
if overweight_obese_population_hypothesis!= overweight_obese_population_premise:
    # check if the percentage in the hypothesis contradicts the percentage reported in the premise
    label = "contradiction"
else:
    # if the hypothesis percentage does not contradict the premise percentage, we can infer entailment
    label = "entailment"

print(label)
