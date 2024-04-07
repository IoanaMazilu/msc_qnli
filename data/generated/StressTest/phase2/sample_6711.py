# Premise: Mike gives you another 17 balls.
# Hypothesis: Mike gives you another less than 77 balls.
# Golden Label: entailment

balls_given_premise = 17
balls_given_hypothesis = 77

# the hypothesis refers to the number of balls given by Mike in the premise
if balls_given_premise >= balls_given_hypothesis:
    # check if the estimate of 'balls_given_hypothesis' contradicts the number of balls given in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

