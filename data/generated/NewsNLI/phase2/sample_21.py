# Premise: 328 Lee Slattery, who held a two-stroke lead as he seeks his first European Tour title.
# Hypothesis: Fellow Englishman Lee Slattery leads by two strokes seeking first title.
# Golden Label: entailment

lead_premise = 2
lead_hypothesis = 2

# the hypothesis mentions the lead held by Lee Slattery, which is also mentioned in the premise
if lead_hypothesis != lead_premise:
    # check if the lead in the hypothesis contradicts the lead reported in the premise
    label = "contradiction"
else:
    # if the lead value in the hypothesis does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)

