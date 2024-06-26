overweight_obese_premise = 0.695
overweight_obese_hypothesis = 0.70

# the hypothesis mentions that nearly 70% of the population is overweight or obese
# the premise mentions that 69.5% of the Mexican population aged 15 and older is overweight or obese
if overweight_obese_hypothesis != overweight_obese_premise:
    # check if the percentage of overweight or obese people in the hypothesis contradicts the percentage reported in the premise
    label = "contradiction"
else:
    # if the hypothesis percentage does not contradict the premise percentage, we can infer entailment
    label = "entailment"

print(label)
