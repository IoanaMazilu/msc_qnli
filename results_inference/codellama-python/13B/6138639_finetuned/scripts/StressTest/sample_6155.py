john_age_difference_premise = 21
john_age_difference_hypothesis = 71

# the hypothesis talks about the age difference between John and Wilson in the future, referenced also in the premise
if john_age_difference_hypothesis!= john_age_difference_premise:
    # check if the age difference in the hypothesis contradicts the age difference mentioned in the premise
    label = "contradiction"
else:
    # the premise gives an exact age difference for the future
    # the age difference in the hypothesis is the same as the one in the premise, so it can be explicitly entailed from the premise
    label = "entailment"

print(label)
