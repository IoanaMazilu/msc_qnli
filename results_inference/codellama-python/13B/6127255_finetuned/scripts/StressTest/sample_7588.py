# Scores in French Language, Geography, Art and design, History and Physical Education respectively
scores_premise = [46, 75, 72, 63, 65]
scores_hypothesis = [86, 75, 72, 63, 65]

# Average mark calculated from the scores
average_mark_premise = sum(scores_premise) / len(scores_premise)
average_mark_hypothesis = sum(scores_hypothesis) / len(scores_hypothesis)

# The hypothesis talks about the average mark calculated from the scores, referenced also in the premise
if average_mark_hypothesis <= average_mark_premise:
    # check if the hypothesis value contradicts the estimate of more than 'average_mark_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the average mark
    # any average mark greater than 'average_mark_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
