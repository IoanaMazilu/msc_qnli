average_shirts_premise = 80
average_shirts_hypothesis = 40

# the hypothesis talks about the average number of shirts with Salman, Ambani and Dalmiya mentioned in the premise
if average_shirts_hypothesis >= average_shirts_premise:
    # check if the hypothesis value contradicts the estimate of less than 'average_shirts_premise'
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
