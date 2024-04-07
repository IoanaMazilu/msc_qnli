# Premise: If Dhoni paid a total of $38, excluding sales tax, to rent the tool, for how many hours did she rent it?
# Hypothesis: If Dhoni paid a total of $more than 38, excluding sales tax, to rent the tool, for how many hours did she rent it?
# Golden Label: contradiction

rent_paid_premise = 38
rent_paid_hypothesis = 38

# the hypothesis refers to the amount paid for renting the tool mentioned in the premise
if rent_paid_hypothesis > rent_paid_premise:
    # check if the hypothesis value contradicts the amount paid in the premise
    label = "contradiction"
else:
    # the hypothesis value does not contradict the premise one, but there is no enough data to infer entailment
    label = "neutral"

print(label)

