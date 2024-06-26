frank_john_difference_premise = 14
frank_john_difference_hypothesis = 84

# the hypothesis refers to the age difference between Frank and John mentioned in the premise
if frank_john_difference_premise > frank_john_difference_hypothesis:
    # check if the age difference from the premise contradicts the estimated age difference from the hypothesis
    label = "contradiction"
elif frank_john_difference_premise == frank_john_difference_hypothesis:
    # check if the age difference from the premise is equal to the estimated age difference from the hypothesis
    label = "entailment"
else:
    # the premise gives a specific age difference
    # any age difference greater than 'frank_john_difference_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
