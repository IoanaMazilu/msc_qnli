# Premise: In Honduras, the law requires anyone transporting the equivalent of more than $10,000 to declare it before authorities and establish where it came from.
# Hypothesis: Anyone transporting more than $10,000 must prove where the money came from, law says.
# Golden Label: entailment

amount_premise = 10000
amount_hypothesis = 10000

# the hypothesis mentions the amount that triggers the need for declaration and proof of source, which is also mentioned in the premise
if amount_hypothesis != amount_premise:
    # check if the amount in the hypothesis contradicts the amount reported in the premise
    label = "contradiction"
else:
    # if the amount in the hypothesis does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)

