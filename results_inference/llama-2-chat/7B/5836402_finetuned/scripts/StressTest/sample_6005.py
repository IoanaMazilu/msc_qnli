balls_needed_premise = 4
balls_needed_hypothesis = 3

# the hypothesis talks about the number of balls John needs, referenced also in the premise
if balls_needed_hypothesis!= balls_needed_premise:
    # check if the number of balls needed in the hypothesis contradicts the number of balls needed in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
