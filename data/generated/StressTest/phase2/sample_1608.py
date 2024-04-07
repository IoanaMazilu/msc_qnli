# Premise: If Dravid paid a total of $38, excluding sales tax, to rent the tool, for how many hours did she rent it?
# Hypothesis: If Dravid paid a total of $less than 88, excluding sales tax, to rent the tool, for how many hours did she rent it?
# Golden Label: entailment

payment_premise = 38
payment_hypothesis = 88

# the hypothesis refers to the total payment made by Dravid mentioned in the premise
if payment_hypothesis < payment_premise:
    # check if the hypothesis value contradicts the actual payment mentioned in the premise
    label = "contradiction"
elif payment_hypothesis == payment_premise:
    # if the hypothesis value is exactly the same as the premise, we can infer entailment
    label = "entailment"
else:
    # if the hypothesis value is greater than the premise but does not contradict it, we can infer neutrality
    label = "neutral"

print(label)

