y_premise = 20
y_hypothesis = 30

# the hypothesis talks about the number of people trapped, which is also mentioned in the premise
if y_hypothesis > y_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif y_hypothesis == y_premise:
    # check if the hypothesis value is equal to the premise value
    label = "entailment"
else:
    # if the hypothesis value is less than the premise value, it does not contradict or entail the premise
    label = "neutral"

print(label)

