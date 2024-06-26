balls_premise = 378
juggler_premise = 1.0
balls_per_juggler_premise = 6

# the hypothesis refers to the number of jugglers needed, which is not mentioned in the premise
# compute the number of jugglers needed based on the premise
jugglers_needed_premise = balls_premise / balls_per_juggler_premise

# check if the number of jugglers needed from the hypothesis contradicts the number of jugglers needed from the premise
if jugglers_needed_premise!= jugglers_hypothesis:
    label = "contradiction"
else:
    label = "entailment"

print(label)
