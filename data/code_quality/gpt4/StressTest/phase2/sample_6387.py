balls_given_premise = 100
balls_given_hypothesis = 300

# the hypothesis refers to the number of balls given by John mentioned in the premise
if balls_given_premise >= balls_given_hypothesis:
    # check if the estimate of 'balls_given_hypothesis' contradicts the number of balls given in the premise
    label = "contradiction"
elif balls_given_premise != balls_given_hypothesis:
    # any number of balls given less than 'balls_given_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
