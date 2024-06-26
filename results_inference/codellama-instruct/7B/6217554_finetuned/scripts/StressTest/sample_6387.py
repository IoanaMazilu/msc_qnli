balls_given_premise = 100
balls_given_hypothesis = 300

# the hypothesis refers to the number of balls given by John, mentioned also in the premise
if balls_given_hypothesis <= balls_given_premise:
    # check if the hypothesis value contradicts the number of balls given in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
