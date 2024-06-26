value_premise = 7/12
value_hypothesis = 5/12

# the hypothesis refers to the same task Anup was asked to do in the premise, but with different values
if value_hypothesis != value_premise:
    # check if the fraction in the hypothesis contradicts the fraction in the premise
    label = "contradiction"
else:
    # if the fractions are the same, we can infer entailment
    label = "entailment"

print(label)
