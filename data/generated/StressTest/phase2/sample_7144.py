# Premise: Scott's average (arithmetic mean) golf score on his first four rounds was less than 48.
# Hypothesis: Scott's average (arithmetic mean) golf score on his first four rounds was 38.
# Golden Label: neutral

average_score_premise = 48
average_score_hypothesis = 38

# the hypothesis also refers to Scott's average golf score on his first four rounds, just like the premise
if average_score_hypothesis >= average_score_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # the premise only states that the average golf score is less than 'average_score_premise'
    # any score less than 'average_score_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
