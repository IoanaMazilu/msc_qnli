points_premise = 26
rebounds_premise = 9
points_hypothesis = 26
rebounds_hypothesis = 9

# the hypothesis talks about the number of points and rebounds Childress made, which is also mentioned in the premise
if points_hypothesis != points_premise:
    # check if the number of points in the hypothesis contradicts the number of points from the premise
    label = "contradiction"
elif rebounds_hypothesis != rebounds_premise:
    # check if the number of rebounds in the hypothesis contradicts the number of rebounds in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
