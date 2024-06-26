day_premise = 7
day_hypothesis = 7

# the hypothesis talks about the day of the week when the train leaves Chennai
if day_hypothesis == day_premise:
    # if the hypothesis and premise refer to the same day of the week, we can infer entailment
    label = "entailment"
elif day_hypothesis < day_premise:
    # if the hypothesis refers to a day earlier than the premise, we can infer contradiction
    label = "contradiction"
else:
    # if the hypothesis and premise refer to different days of the week, we can infer neutrality
    label = "neutral"

print(label)
