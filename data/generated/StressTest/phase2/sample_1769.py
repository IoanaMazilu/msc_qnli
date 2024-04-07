# Premise: If Jadeja paid a total of $133, excluding sales tax, to rent the tool, for how many hours did she rent it?
# Hypothesis: If Jadeja paid a total of $233, excluding sales tax, to rent the tool, for how many hours did she rent it?
# Golden Label: contradiction

payment_premise = 133
payment_hypothesis = 233

# the hypothesis refers to the amount Jadeja paid in the premise
if payment_premise != payment_hypothesis:
    # check if the amount in the hypothesis contradicts the amount in the premise
    label = "contradiction"
else:
    # the premise and hypothesis amounts are equal
    label = "entailment"

print(label)

