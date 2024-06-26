balls_given_premise = 17
balls_given_hypothesis = 77

# the hypothesis refers to the number of balls given by Mike, mentioned in the premise
if balls_given_premise >= balls_given_hypothesis:
    # check if the number of balls given in the premise contradicts the estimate of less than 'balls_given_hypothesis'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
