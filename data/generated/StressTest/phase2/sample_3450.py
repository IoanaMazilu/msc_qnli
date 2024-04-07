# Premise: Jose joined him 2 months later, investing Rs.
# Hypothesis: Jose joined him less than 8 months later, investing Rs.
# Golden Label: entailment

months_premise = 2
months_hypothesis = 8

# the hypothesis refers to the number of months Jose joined later which is also mentioned in the premise
if months_premise > months_hypothesis:
    # check if the premise value contradicts the estimate of less than 'months_hypothesis'
    label = "contradiction"
elif months_premise == months_hypothesis:
    # if the premise value equals the hypothesis value, it contradicts the "less than" statement in the hypothesis
    label = "contradiction"
else:
    # the premise gives a specific month number, any number of months greater than 'months_premise' is consistent with the premise, but it cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

