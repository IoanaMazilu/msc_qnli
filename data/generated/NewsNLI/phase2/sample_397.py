# Premise: Three children, aged three and four, were among the 16 people killed, according to state-run newspaper Jornal de Angola.
# Hypothesis: Three children were among those killed, state-run newspaper reports.
# Golden Label: entailment

children_premise = 3
children_hypothesis = 3

# the hypothesis mentions the killing of three children, which is also mentioned in the premise
# however, the hypothesis does not mention the total number of people killed or the children's age, which are stated in the premise
if children_hypothesis != children_premise:
    # check if the number of children in the hypothesis contradicts the number of children mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer neutrality
    label = "neutral"

print(label)

