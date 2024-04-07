# Premise: Frank is less than 42 years younger then John.
# Hypothesis: Frank is 12 years younger then John.
# Golden Label: neutral

frank_age_difference_premise = 42
frank_age_difference_hypothesis = 12

# the hypothesis talks about the age difference between Frank and John, which is also mentioned in the premise
if frank_age_difference_hypothesis > frank_age_difference_premise:
    # check if the hypothesis value contradicts the estimate of less than 'frank_age_difference_premise'
    label = "contradiction"
elif frank_age_difference_hypothesis < frank_age_difference_premise:
    # any age difference less than 'frank_age_difference_premise' is explicitly entailed from the premise
    label = "entailment"
else:
    # the premise and the hypothesis agree exactly on the age difference
    label = "entailment"

print(label)

