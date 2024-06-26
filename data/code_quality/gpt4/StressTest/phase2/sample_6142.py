average_score_premise = 48
average_score_hypothesis = 18

# the hypothesis refers to the average golf score of Scott mentioned in the premise
if average_score_hypothesis >= average_score_premise:
    # check if the hypothesis contradicts the premise statement of the average score being less than 'average_score_premise'
    label = "contradiction"
elif average_score_hypothesis > 0:
    # a score of 0 would be impossible in golf, so we can assume the average score is more than 0
    # if the average score in the hypothesis is more than 0 and less than the average score in the premise, it is consistent with the premise
    label = "entailment"
else:
    # if none of the above conditions are met, the relation is neutral
    label = "neutral"

print(label)
