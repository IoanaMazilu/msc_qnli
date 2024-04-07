# Premise: Lee Colle insures its students for thefts up to $1000.
# Hypothesis: Lee Colle insures its students for thefts up to $less than 2000.
# Golden Label: entailment

insurance_premise = 1000
insurance_hypothesis = 2000

# the hypothesis refers to the insurance amount for thefts at Lee Colle, as mentioned in the premise
if insurance_hypothesis < insurance_premise:
    # check if the insurance amount in the hypothesis contradicts the insurance amount reported in the premise
    label = "contradiction"
elif insurance_hypothesis > insurance_premise:
    # the hypothesis insurance amount is greater than the premise one
    # therefore, it's consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the insurance amount in the hypothesis is equal to the one in the premise, we can infer entailment
    label = "entailment"

print(label)

