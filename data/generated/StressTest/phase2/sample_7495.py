# Premise: Jane started baby-sitting when she was less than 88 years old.
# Hypothesis: Jane started baby-sitting when she was 18 years old.
# Golden Label: neutral

baby_sitting_age_premise = 88
baby_sitting_age_hypothesis = 18

# the hypothesis talks about Jane's age when she started baby-sitting, which is also referenced in the premise
if baby_sitting_age_hypothesis >= baby_sitting_age_premise:
    # check if the hypothesis age contradicts the premise of less than 'baby_sitting_age_premise'
    label = "contradiction"
elif baby_sitting_age_hypothesis < baby_sitting_age_premise:
    # the premise suggests that Jane started baby-sitting at an age less than 'baby_sitting_age_premise'
    # any age less than 'baby_sitting_age_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

