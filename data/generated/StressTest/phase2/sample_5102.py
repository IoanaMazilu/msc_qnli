# Premise: 5887 is divided between Shyam and Ram, such that Shyam's share at the end of 9 years is equal to Ram's share at the end of 11 years, compounded annually at the rate of 5 %.
# Hypothesis: more than 5887 is divided between Shyam and Ram, such that Shyam's share at the end of 9 years is equal to Ram's share at the end of 11 years, compounded annually at the rate of 5 %.
# Golden Label: contradiction

amount_premise = 5887
amount_hypothesis = 5887

# the hypothesis makes the same claim as the premise, but with a different amount
if amount_hypothesis != amount_premise:
    # check if the amount in the hypothesis contradicts the amount in the premise
    label = "contradiction"
else:
    # the hypothesis does not make any claims that contradict the premise, but it also doesn't provide any new information that can be entailed from the premise
    label = "neutral"

print(label)

