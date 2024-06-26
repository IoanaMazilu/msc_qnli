earned_premise = 210
earned_hypothesis = 210

# the hypothesis talks about the number of hours worked by Michael, which is also mentioned in the premise
if earned_hypothesis == earned_premise:
    # check if the hypothesis value is equal to the estimate in the premise
    label = "entailment"
elif earned_hypothesis > earned_premise:
    # check if the hypothesis value contradicts the estimate in the premise
    label = "contradiction"
else:
    # if the hypothesis value is neither equal nor greater than the estimate in the premise, we cannot infer any relation
    label = "neutral"

print(label)
