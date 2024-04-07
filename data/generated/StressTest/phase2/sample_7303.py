# Premise: Scott's average (arithmetic mean) golf score on his first four rounds was less than 88.
# Hypothesis: Scott's average (arithmetic mean) golf score on his first four rounds was 58.
# Golden Label: neutral

average_score_premise = 88
average_score_hypothesis = 58

# the hypothesis is about Scott's average golf score, referenced in the premise as well
if average_score_hypothesis >= average_score_premise:
    # check if the hypothesis value contradicts the premise (less than 'average_score_premise')
    label = "contradiction"
else:
    # the premise gives only an upper bound for the average score
    # any average score less than 'average_score_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

