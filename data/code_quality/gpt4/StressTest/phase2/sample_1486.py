average_score_premise = 47
average_score_hypothesis = 17

# The hypothesis speaks about the average marks scored by Ganesh in certain subjects, referenced also in the premise
if average_score_hypothesis >= average_score_premise:
    # check if the hypothesis value contradicts the premise which estimates less than 'average_score_premise'
    label = "contradiction"
elif average_score_hypothesis < average_score_premise:
    # The premise gives an estimate for the average score
    # any average score less than 'average_score_premise' is consistent with the premise, but the specific 'average_score_hypothesis' cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
