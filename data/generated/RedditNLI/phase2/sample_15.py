# Premise: Bush in 2002: We want 5.5 million more homeowners by 2010 & less words in the closing papers they have to sign.
# Hypothesis: President Bush on Homeownership in 2002: 5.5 million more homeowners by 2010 & much less words in their closing documents (seriously))
# Golden Label: entailment

homeowners_premise = 5.5e6
homeowners_hypothesis = 5.5e6

# the hypothesis and premise mention the number of homeowners that President Bush wanted in 2010
if homeowners_hypothesis != homeowners_premise:
    # check if the number of homeowners in the hypothesis contradicts the number of homeowners in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

