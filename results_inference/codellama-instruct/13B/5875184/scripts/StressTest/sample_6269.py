premise_percentage = 10
hypothesis_percentage = 20

# the hypothesis refers to the number of people who died by bombardment and the number of people who left the village on account of fear
if hypothesis_percentage <= premise_percentage:
    # check if the estimate of 'hypothesis_percentage' contradicts the number of people who died by bombardment in the premise
    label = "contradiction"
elif hypothesis_percentage - premise_percentage >= 10:
    # check if the difference between the hypothesis and premise values is greater than 10%
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer neutrality
    label = "neutral"

print(label)
