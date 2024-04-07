# Premise: Dan leaves City A 60 minutes after Cara.
# Hypothesis: Dan leaves City A less than 60 minutes after Cara.
# Golden Label: contradiction

leave_time_premise = 60
leave_time_hypothesis = 60

# the hypothesis refers to the time Dan leaves the city after Cara, mentioned also in the premise
if leave_time_hypothesis >= leave_time_premise:
    # check if the hypothesis time contradicts the premise
    label = "contradiction"
else:
    # the hypothesis suggests a time less than the one in the premise, therefore no entailment can be inferred
    label = "neutral"

print(label)

