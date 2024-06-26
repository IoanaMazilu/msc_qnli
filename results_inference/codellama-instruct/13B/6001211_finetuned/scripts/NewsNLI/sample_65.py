bacteria_premise = 0.28
bacteria_hypothesis = 0.25

# the hypothesis mentions the percentage of Londoners with E. coli bacteria on their hands, which is also mentioned in the premise
if bacteria_hypothesis > bacteria_premise:
    # check if the percentage in the hypothesis contradicts the percentage reported in the premise
    label = "contradiction"
else:
    # if the hypothesis percentage does not contradict the premise percentage, we can infer entailment
    label = "entailment"

print(label)
