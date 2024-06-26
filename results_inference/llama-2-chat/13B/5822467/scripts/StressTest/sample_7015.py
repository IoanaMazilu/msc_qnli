lewis_age_premise = 6
brown_age_premise = 2
lewis_age_hypothesis = 1
brown_age_hypothesis = 2

# the hypothesis refers to the ratio of their ages
if lewis_age_hypothesis / brown_age_hypothesis == lewis_age_premise / brown_age_premise:
    # the hypothesis is consistent with the premise
    label = "neutral"
else:
    # the hypothesis contradicts the premise
    label = "contradiction"

print(label)
