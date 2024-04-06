# Premise: President Bush on Homeownership in 2002: 5.5 million more homeowners by 2010 & much less words in their closing documents (seriously))
# Hypothesis: Bush in 2002: We want 5.5 million more homeowners by 2010 & less words in the closing papers they have to sign.
# Golden Label: entailment

number_homeowners_premise = 5.5
number_homeowners_hypothesis = 5.5

# the hypothesis and premise mention the expected increase in the number of homeowners by 2010
if number_homeowners_hypothesis != number_homeowners_premise:
    # check if the number of homeowners in the hypothesis contradicts the number of homeowners in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

