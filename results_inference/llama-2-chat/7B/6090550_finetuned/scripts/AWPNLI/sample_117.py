y_premise = 25.0
x_premise = 5.0
y_hypothesis = 4.0

# the hypothesis refers to the duration of jogging, which is also mentioned in the premise
# compute the total hours jogged in the premise
total_hours_premise = y_premise / x_premise
if y_hypothesis!= total_hours_premise:
    # check if the duration in the hypothesis contradicts the duration in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
