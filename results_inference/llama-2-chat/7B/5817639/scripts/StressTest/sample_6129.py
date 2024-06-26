x_per_hour_premise = float(input_premise.split(" dollars per hour for the first ")[1])
x_per_hour_hypothesis = float(input_hypothesis.split(" dollars per hour for the first ")[1])

# check if the hypothesis value contradicts the estimate of 'x_per_hour_premise'
if x_per_hour_hypothesis <= x_per_hour_premise:
    label = "contradiction"
elif x_per_hour_hypothesis > x_per_hour_premise + 11:
    # check if the number of additional hours worked in the hypothesis contradicts the estimate of more than 11 hours in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
