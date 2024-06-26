balls_premise = 378
jugglers_hypothesis = 63.0

# the hypothesis refers to the number of jugglers, which is not directly mentioned in the premise
# but we can infer the number of balls juggled at a time from the premise
juggles_premise = 6

# compute the total number of balls juggled by the hypothesis
total_balls_hypothesis = juggles_premise * jugglers_hypothesis

if total_balls_hypothesis!= balls_premise:
    # check if the total number of balls in the hypothesis contradicts the number of balls in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
