balls_premise = 378
juggler_premise = 1
balls_per_juggler_premise = 6
juggler_hypothesis = 63

# the hypothesis talks about the number of jugglers, which is also referenced in the premise
# compute the total number of jugglers needed from the premise
total_juggler_premise = balls_premise // balls_per_juggler_premise
if juggler_hypothesis!= total_juggler_premise:
    # check if the number of jugglers from the hypothesis contradicts the number of jugglers from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"
    
print(label)
