y_future_premise = 18
y_future_hypothesis = 18
y_past_premise = 7
y_past_hypothesis = 7

# the hypothesis talks about Molly's age in more than 18 years, which is also mentioned in the premise
if y_future_hypothesis!= y_future_premise:
    # check if the number of years in the future in the hypothesis contradicts the number of years in the future in the premise
    label = "contradiction"
elif y_past_hypothesis!= y_past_premise:
    # check if the number of years in the past in the hypothesis contradicts the number of years in the past in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
