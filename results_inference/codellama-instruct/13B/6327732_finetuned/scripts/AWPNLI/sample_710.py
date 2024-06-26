balls_premise = 378
juggler_premise = 1.0
balls_per_juggler_premise = 6

juggler_hypothesis = 63.0

# the hypothesis refers to the number of jugglers, which are also mentioned in the premise
# compute the total number of balls that can be juggled by the jugglers in the hypothesis
total_balls_hypothesis = juggler_hypothesis * balls_per_juggler_premise
if total_balls_hypothesis!= balls_premise:
    # check if the number of balls in the hypothesis contradicts the number of balls from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
