# define the scores in the premise
scores_premise = [1, 2, 3, 4, 5]

# define the scores in the hypothesis
scores_hypothesis = [7, 2, 3, 4, 5]

# variable for the lowest score in the hypothesis
lowest_score_hypothesis = min(scores_hypothesis)

# variable for the highest score in the premise
highest_score_premise = max(scores_premise)

# if the lowest score in the hypothesis is less than or equal to the highest score in the premise
# then it's a contradiction because Mary can't get a score less than 1
if lowest_score_hypothesis <= highest_score_premise:
    label = "contradiction"
else:
    # the premise gives only an estimate for the scores
    # any scores less than 7 is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
