# Premise: The next act involved several jugglers, and each juggler is juggling 6.0 balls at a time.
# Hypothesis: 2268.0 balls are needed if there are 378.0 jugglers putting a show at the same time.
# Golden Label: entailment

balls_per_juggler_premise = 6.0
total_balls_hypothesis = 2268.0
jugglers_hypothesis = 378.0

# the hypothesis refers to the number of balls, which are also mentioned in the premise
# compute the total number of balls needed in the premise
total_balls_premise = balls_per_juggler_premise * jugglers_hypothesis

if total_balls_hypothesis != total_balls_premise:
    # check if the number of balls needed in the hypothesis contradicts the number of balls from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

