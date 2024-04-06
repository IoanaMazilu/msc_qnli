# Premise: But only one in three Americans are concerned that a bridge that they drive across regularly will collapse, while 69 percent are not worried.
# Hypothesis: Fifty-two percent of Americans worried that a bridge will collapse in the U.S.
# Golden Label: neutral

concerned_americans_premise = 1/3 * 100  # converting the fraction into percentage
concerned_americans_hypothesis = 52

# the hypothesis mentions the percentage of Americans who are worried about a bridge collapsing, which is also referenced in the premise
if concerned_americans_hypothesis != concerned_americans_premise:
    # check if the percentage of concerned Americans in the hypothesis contradicts the percentage in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

