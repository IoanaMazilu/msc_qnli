yhat_premise = 4
yhat_hypothesis = 7

# the hypothesis talks about the number of apples Maddie has, which is also mentioned in the premise
if yhat_premise >= yhat_hypothesis:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif yhat_premise < yhat_hypothesis:
    # if the hypothesis value is less than the premise value, we can infer entailment
    label = "entailment"
else:
    # if the hypothesis value is equal to the premise value, we can infer neutral
    label = "neutral"

print(label)

