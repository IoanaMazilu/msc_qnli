balls_premise = 378
juggler_premise = 1
balls_per_juggler_premise = 6
juggler_hypothesis = 63

# the hypothesis refers to the number of jugglers, which is not mentioned in the premise
# compute the total number of balls that can be juggled by the number of jugglers in the premise
total_balls_premise = balls_premise / juggler_premise
if total_balls_premise!= balls_per_juggler_premise:
    # check if the number of balls that can be juggled by the number of jugglers in the premise contradicts the estimate of 6 balls per juggler
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
