# Premise: Deepa bought a calculator at 30% discount on the listed price.
# Hypothesis: Deepa bought a calculator at more than 10% discount on the listed price.
# Golden Label: entailment

discount_premise = 30
discount_hypothesis = 10

# the hypothesis talks about the discount on a calculator, which is also referenced in the premise
if discount_premise < discount_hypothesis:
    # check if the discount in the premise contradicts the minimum discount in the hypothesis
    label = "contradiction"
elif discount_premise == discount_hypothesis:
    # if the discount in the premise equals the one in the hypothesis, it cannot be "more than" as stated in the hypothesis
    label = "contradiction"
else:
    # if the discount in the premise is more than the one in the hypothesis, we can infer entailment
    label = "entailment"

print(label)

