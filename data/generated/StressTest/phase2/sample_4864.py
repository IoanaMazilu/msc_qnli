# Premise: Mary is more than 1 years younger than Albert.
# Hypothesis: Mary is 8 years younger than Albert.
# Golden Label: neutral

mary_age_diff_premise = 1
mary_age_diff_hypothesis = 8

# the hypothesis talks about the difference in age between Mary and Albert, also mentioned in the premise
if mary_age_diff_hypothesis <= mary_age_diff_premise:
    # check if the hypothesis value contradicts the statement of 'mary_age_diff_premise'
    label = "contradiction"
else:
    # the premise gives only a minimum difference in age
    # any difference greater than 'mary_age_diff_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

