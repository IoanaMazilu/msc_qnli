# Premise: Jane started baby-sitting when she was less than 58 years old.
# Hypothesis: Jane started baby-sitting when she was 18 years old.
# Golden Label: neutral

babysitting_age_premise = 58
babysitting_age_hypothesis = 18

# the hypothesis refers to the age Jane started babysitting, which is also mentioned in the premise
if babysitting_age_hypothesis >= babysitting_age_premise:
    # if the hypothesized age contradicts the premise that Jane started babysitting at an age less than 'babysitting_age_premise'
    label = "contradiction"
elif babysitting_age_hypothesis < babysitting_age_premise:
    # any age less than 'babysitting_age_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

