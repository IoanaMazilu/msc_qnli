balloons_blew_up_premise = 47.0
balloons_blew_up_hypothesis = 13.0
total_balloons_premise = balloons_blew_up_premise + balloons_blew_up_hypothesis
if total_balloons_hypothesis!= total_balloons_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
