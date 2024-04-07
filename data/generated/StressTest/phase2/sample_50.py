# Premise: Sarah signed 1/2 of the Christmas cards, and Richard signed 3/8 of them.
# Hypothesis: Sarah signed 6/2 of the Christmas cards, and Richard signed 3/8 of them.
# Golden Label: contradiction

sarah_signed_premise = 1/2
sarah_signed_hypothesis = 6/2
richard_signed_premise = 3/8
richard_signed_hypothesis = 3/8

# the hypothesis talks about the number of Christmas cards signed by Sarah and Richard, referenced also in the premise
if sarah_signed_hypothesis != sarah_signed_premise:
    # check if the fraction of Christmas cards signed by Sarah in the hypothesis contradicts the fraction in the premise
    label = "contradiction"
elif richard_signed_hypothesis != richard_signed_premise:
    # check if the fraction of Christmas cards signed by Richard in the hypothesis contradicts the fraction in the premise
    label = "contradiction"
else:
    # if the hypothesis values are the same with the premise ones, we can infer entailment
    label = "entailment"

print(label)

