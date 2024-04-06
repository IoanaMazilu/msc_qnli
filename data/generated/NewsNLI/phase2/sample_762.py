# Premise: But the prosecutor's office estimated the value of the lost works at 500 million euros ($617 million.)
# Hypothesis: Works are worth about 100 million euros ($123.7 million)
# Golden Label: neutral

value_lost_works_premise = 500000000
value_lost_works_hypothesis = 100000000

# the hypothesis mentions the value of the lost works, which is also referenced in the premise
if value_lost_works_hypothesis != value_lost_works_premise:
    # check if the value of the lost works in the hypothesis contradicts the value of the lost works in the premise
    label = "contradiction"
else:
    # if the value of the lost works in the hypothesis does not contradict the value of the lost works in the premise, we can infer entailment
    label = "entailment"

print(label)

