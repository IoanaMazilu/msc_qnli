jerry_average_premise = 80 # premise gives Jerry's current average
jerry_average_hypothesis = 85 # hypothesis talks about raising Jerry's average by more than 2 points

# check if the hypothesis value contradicts the premise
if jerry_average_hypothesis > jerry_average_premise + 2:
    label = "contradiction"
elif jerry_average_hypothesis == jerry_average_premise + 2:
    # check if the hypothesis value entails the premise
    label = "entailment"
else:
    # the hypothesis value is not contradictory to the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
