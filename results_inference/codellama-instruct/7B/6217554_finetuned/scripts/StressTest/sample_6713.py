balls_given_premise = 17
balls_given_hypothesis = 77

# the hypothesis talks about the number of balls given by Mike, referenced also in the premise
if balls_given_hypothesis!= balls_given_premise:
    # check if the number of balls given in the hypothesis contradicts the number of balls given in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
