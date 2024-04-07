# Premise: Today John is less than 8 times older than Mark.
# Hypothesis: Today John is 3 times older than Mark.
# Golden Label: neutral

john_age_multiple_premise = 8
john_age_multiple_hypothesis = 3

# the hypothesis talks about John's age in relation to Mark's, also referenced in the premise
if john_age_multiple_hypothesis >= john_age_multiple_premise:
    # check if the value in the hypothesis contradicts the estimate of less than 'john_age_multiple_premise'
    label = "contradiction"
elif john_age_multiple_hypothesis < john_age_multiple_premise:
    # if John's age multiple in hypothesis is less than the premise, it's consistent with the premise
    # but we cannot explicitly entail it from the premise because we don't know the exact multiple in the premise
    label = "neutral"

print(label)

