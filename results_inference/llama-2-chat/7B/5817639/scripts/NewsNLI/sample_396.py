victims_premise = ["two women", "two men"]
victims_hypothesis = ["two men", "two women"]

# the hypothesis mentions the same number and gender of victims as the premise
if victims_hypothesis == victims_premise:
    # if the hypothesis and premise match, we can infer entailment
    label = "entailment"
elif any(v1!= v2 for v1, v2 in zip(victims_hypothesis, victims_premise)):
    # if the victims' genders or numbers do not match in the hypothesis and premise, we can infer contradiction
    label = "contradiction"
else:
    # if the hypothesis and premise do not provide enough information to determine entailment or contradiction, we can infer neutrality
    label = "neutral"

print(label)
