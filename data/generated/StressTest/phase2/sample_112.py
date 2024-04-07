# Premise: Bruce and Anne can clean their house in more than 1 hours working together at their respective constant rates.
# Hypothesis: Bruce and Anne can clean their house in 4 hours working together at their respective constant rates.
# Golden Label: neutral

cleaning_time_premise = 1
cleaning_time_hypothesis = 4

# the hypothesis refers to the cleaning time mentioned in the premise
if cleaning_time_hypothesis <= cleaning_time_premise:
    # check if the cleaning time in the hypothesis contradicts the premise's estimate of more than 'cleaning_time_premise' hours
    label = "contradiction"
else:
    # the premise only gives an estimate for the cleaning time
    # any cleaning time greater than 'cleaning_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

