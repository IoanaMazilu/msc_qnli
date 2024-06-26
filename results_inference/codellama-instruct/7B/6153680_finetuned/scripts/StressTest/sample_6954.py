average_shirts_premise = 40
average_shirts_hypothesis = 80

# the hypothesis talks about the average number of shirts with Salman, Ambani and Dalmiya, which is also mentioned in the premise
if average_shirts_hypothesis <= average_shirts_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
