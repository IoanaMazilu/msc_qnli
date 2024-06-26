needed_balls_premise = 3
needed_balls_hypothesis = 4
total_balls_premise = 10
total_balls_hypothesis = 10

# the hypothesis talks about the number of balls John needs, referenced also in the premise
if needed_balls_hypothesis <= needed_balls_premise:
    # check if the hypothesis value contradicts the estimate of more than 'needed_balls_premise'
    label = "contradiction"
elif needed_balls_hypothesis > total_balls_premise:
    # check if the number of balls in the hypothesis contradicts the total number of balls in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
