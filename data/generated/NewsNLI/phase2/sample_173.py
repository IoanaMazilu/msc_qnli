# Premise: The other four main parties followed with narrow margins separating them.
# Hypothesis: Five main parties lead with narrow margins separating thm.
# Golden Label: entailment

parties_premise = 4
parties_hypothesis = 5

# the hypothesis mentions the number of main parties, which is also referenced in the premise
if parties_hypothesis != parties_premise:
    # check if the number of parties in the hypothesis contradicts the number of parties in the premise
    label = "contradiction"
else:
    # if the number of parties in the hypothesis does not contradict the number in the premise, we can infer entailment
    label = "entailment"

print(label)

