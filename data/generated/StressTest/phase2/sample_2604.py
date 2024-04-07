# Premise: The ratio of men to women in the Snyder community choir is 4 to 6.
# Hypothesis: The ratio of men to women in the Snyder community choir is less than 6 to 6.
# Golden Label: entailment

men_premise = 4
women_premise = 6
men_hypothesis = 6
women_hypothesis = 6

# the hypothesis refers to the ratio of men to women in the choir, which is also mentioned in the premise
if men_premise/men_hypothesis >= women_premise/women_hypothesis:
    # check if the ratio of men to women in the hypothesis contradicts the ratio of men to women in the premise
    label = "contradiction"
else:
    # if the ratios do not contradict, we can infer entailment
    label = "entailment"

print(label)

