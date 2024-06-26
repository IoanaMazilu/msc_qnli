 score_premise = 2
score_hypothesis = 6

# the hypothesis talks about the score Jerry must earn on the fourth test to raise his average by'score_hypothesis' points
if score_hypothesis <= score_premise:
    # check if the hypothesis value contradicts the score in the premise
    label = "contradiction"
else:
    # the premise gives an exact score for the average increase
    # any score less than'score_premise' contradicts the premise
    label = "contradiction"

print(label)
