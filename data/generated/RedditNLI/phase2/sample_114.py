# Premise: Fed to launch QE3 of $40 billion MBS each month.
# Hypothesis: Fed Undertakes QE3 With $40 Billion in MBS Purchases a Month.
# Golden Label: entailment

qe3_premise = 40
qe3_hypothesis = 40

# the hypothesis and premise both mention the amount in billions of MBS purchases each month for QE3
if qe3_hypothesis != qe3_premise:
    # check if the amount in the hypothesis contradicts the amount in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

