total_hours_premise = 3
total_hours_hypothesis = 4

# the hypothesis refers to the total hours of jogging and walking mentioned in the premise
if total_hours_premise >= total_hours_hypothesis:
    # check if the estimate of 'total_hours_premise' contradicts the maximum total hours in the hypothesis
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
