coffee_premise = 115
coffee_hypothesis = 315

# the hypothesis talks about the amount of coffee Carina has, referenced also in the premise
if coffee_hypothesis != coffee_premise:
    # check if the amount of coffee in the hypothesis contradicts the amount of coffee reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
