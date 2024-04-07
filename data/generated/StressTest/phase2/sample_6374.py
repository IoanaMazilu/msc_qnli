# Premise: Shreehari has 125 pencils.
# Hypothesis: Shreehari has 525 pencils.
# Golden Label: contradiction

pencils_premise = 125
pencils_hypothesis = 525

# the hypothesis refers to the number of pencils Shreehari has, which is also mentioned in the premise
if pencils_hypothesis != pencils_premise:
    # check if the number of pencils in the hypothesis contradicts the number of pencils in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

