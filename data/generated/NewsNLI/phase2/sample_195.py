# Premise: Thirty-six survivors have been rescued from the Aegean Sea, and the search is continuing, Katherine Tenta of the Greek coast guard told CNN by phone.
# Hypothesis: Greek coast guard has rescued 36 survivors, and a search operation is under way.
# Golden Label: entailment

survivors_rescued_premise = 36
survivors_rescued_hypothesis = 36

# the hypothesis mentions the number of survivors rescued, which is also mentioned in the premise
if survivors_rescued_hypothesis != survivors_rescued_premise:
    # check if the number of survivors rescued in the hypothesis contradicts the number of survivors rescued in the premise
    label = "contradiction"
else:
    # if the number of survivors rescued in the hypothesis does not contradict the number of survivors rescued in the premise, we can infer entailment
    label = "entailment"

print(label)

