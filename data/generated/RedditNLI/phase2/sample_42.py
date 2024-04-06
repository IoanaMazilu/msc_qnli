# Premise: It will take black families 228 years to amass the wealth that white families have today, new study finds.
# Hypothesis: It Would Take 228 Years for Black Families to Amass Wealth of White Families, Analysis Says.
# Golden Label: entailment

years_for_wealth_premise = 228
years_for_wealth_hypothesis = 228

# the hypothesis and premise mention the number of years it would take for black families to amass the wealth of white families
if years_for_wealth_hypothesis != years_for_wealth_premise:
    # check if the number of years in the hypothesis contradicts the number of years in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

