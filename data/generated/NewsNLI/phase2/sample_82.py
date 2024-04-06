# Premise: The study finds that while two-thirds of Latino voters support the Democrats, 22 percent back the Republican candidate.
# Hypothesis: Pew study:Nearly two-thirds of Latinos support Democrats ; 22 percent back GOP.
# Golden Label: entailment

democrats_support_premise = 2/3
republican_support_premise = 0.22
democrats_support_hypothesis = 2/3
republican_support_hypothesis = 0.22

# the hypothesis mentions the proportion of Latino voters supporting Democrats and Republicans, which are also mentioned in the premise
if democrats_support_hypothesis != democrats_support_premise:
    # check if the democratic support in the hypothesis contradicts the democratic support reported in the premise
    label = "contradiction"
elif republican_support_hypothesis != republican_support_premise:
    # check if the republican support from the hypothesis contradicts the republican support in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

