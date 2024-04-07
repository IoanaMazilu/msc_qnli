# Premise: Mary is less than 40 years younger than Albert.
# Hypothesis: Mary is 10 years younger than Albert.
# Golden Label: neutral

mary_age_diff_premise = 40
mary_age_diff_hypothesis = 10

# the hypothesis refers to the age difference between Mary and Albert also stated in the premise
if mary_age_diff_hypothesis > mary_age_diff_premise:
    # check if the hypothesis value contradicts the premise estimate of less than 'mary_age_diff_premise'
    label = "contradiction"
elif mary_age_diff_hypothesis < mary_age_diff_premise:
    # the premise gives only an upper limit for the age difference
    # any age difference less than 'mary_age_diff_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the age difference in the hypothesis equals the upper limit in the premise, we can infer entailment
    label = "entailment"

print(label)

