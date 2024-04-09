premise_train_time = 12
hypothesis_train_time = 11

# the hypothesis refers to the time of departure of the train from Chennai
if hypothesis_train_time < premise_train_time:
    # the hypothesis contradicts the premise, as the train departs earlier in the hypothesis than in the premise
    label = "contradiction"
elif hypothesis_train_time == premise_train_time:
    # the hypothesis and premise are consistent, but the hypothesis does not entail the premise
    label = "neutral"
else:
    # the hypothesis does not contradict the premise, but the premise does not explicitly entail the hypothesis
    label = "neutral"

print(label)
