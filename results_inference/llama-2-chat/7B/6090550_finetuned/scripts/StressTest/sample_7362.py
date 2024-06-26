y_premise = 30%
y_hypothesis = 10%

# the hypothesis refers to the discount on the listed price of the calculator, which is also mentioned in the premise
if y_premise <= y_hypothesis:
    # check if the discount in the premise contradicts the discount in the hypothesis
    label = "contradiction"
else:
    # if the discount in the premise is more than the discount in the hypothesis, we can infer entailment
    label = "entailment"

print(label)
