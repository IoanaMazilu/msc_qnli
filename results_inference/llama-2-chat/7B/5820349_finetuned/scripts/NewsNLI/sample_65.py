e_coli_premise = 0.28
e_coli_hypothesis = 1 / 4

# the hypothesis refers to the percentage of Londoners with E. coli bacteria, which is also mentioned in the premise
# we can directly compare the percentages in the premise and the hypothesis
if e_coli_hypothesis > e_coli_premise:
    # check if the percentage in the hypothesis contradicts the percentage reported in the premise
    label = "contradiction"
else:
    # if the hypothesis percentage does not contradict the premise percentage, we can infer entailment
    label = "entailment"

print(label)
