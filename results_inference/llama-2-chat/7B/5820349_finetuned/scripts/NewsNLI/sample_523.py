percentage_premise = 69.5
percentage_hypothesis = 70

# the hypothesis mentions the percentage of the population that is overweight or obese, which is also referenced in the premise
if percentage_hypothesis!= percentage_premise:
    # check if the percentage in the hypothesis contradicts the percentage reported in the premise
    label = "contradiction"
else:
    # if the hypothesis percentage does not contradict the premise percentage, we can infer entailment
    label = "entailment"

print(label)
