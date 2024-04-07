# Premise: Gordon buys 5 dolls for his 5 nieces.
# Hypothesis: Gordon buys more than 3 dolls for his 5 nieces.
# Golden Label: entailment

dolls_purchased_premise = 5
dolls_purchased_hypothesis = 3

# the hypothesis refers to the number of dolls Gordon buys for his nieces, which is also mentioned in the premise
if dolls_purchased_hypothesis >= dolls_purchased_premise:
    # check if the hypothesis value contradicts the number of dolls purchased in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)

