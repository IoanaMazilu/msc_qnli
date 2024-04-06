# Premise: You have 378 balls and 1.0 juggler is able to juggle 6 balls at a time.
# Hypothesis: You need 67.0 jugglers.
# Golden Label: contradiction

balls_premise = 378
juggle_capacity_premise = 6
jugglers_hypothesis = 67.0

# the hypothesis refers to the number of jugglers needed, which can be calculated from the premise
# compute the number of jugglers needed from the premise
jugglers_premise = balls_premise / juggle_capacity_premise

if jugglers_hypothesis != jugglers_premise:
    # check if the number of jugglers in the hypothesis contradicts the number of jugglers calculated from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

