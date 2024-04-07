# Premise: Frank is 12 years younger then John.
# Hypothesis: Frank is less than 42 years younger then John.
# Golden Label: entailment

frank_age_difference_premise = 12
frank_age_difference_hypothesis = 42

# the hypothesis refers to the age difference between Frank and John mentioned in the premise
if frank_age_difference_premise >= frank_age_difference_hypothesis:
    # check if the age difference in the premise contradicts 'frank_age_difference_hypothesis'
    label = "contradiction"
elif frank_age_difference_premise > frank_age_difference_hypothesis:
    # check if the age difference in the premise contradicts 'frank_age_difference_hypothesis'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

