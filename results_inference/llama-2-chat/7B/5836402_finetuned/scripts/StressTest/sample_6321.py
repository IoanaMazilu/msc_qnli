amateurs_premise = 4
amateurs_hypothesis = 8

# the hypothesis refers to the number of chess amateurs playing in Villa's chess club tournament, which is also mentioned in the premise
if amateurs_premise >= amateurs_hypothesis:
    # check if the estimate of 'amateurs_hypothesis' contradicts the number of chess amateurs in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
