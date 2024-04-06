# Premise: Team captain Butt said Pakistan gave 100 percent throughout a match.
# Hypothesis: Everyone on the team gave'' 100 percent,'' captain Salman Butt says.
# Golden Label: entailment

effort_premise = 100
effort_hypothesis = 100

# the hypothesis mentions the effort given by the team, which is also mentioned in the premise
if effort_hypothesis != effort_premise:
    # check if the effort percentage in the hypothesis contradicts the effort percentage reported in the premise
    label = "contradiction"
else:
    # if the effort percentage in the hypothesis does not contradict the effort percentage in the premise, we can infer entailment
    label = "entailment"

print(label)

