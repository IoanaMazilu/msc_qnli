boys_percentage_premise = 30
boys_percentage_hypothesis = 10

# the hypothesis refers to the percentage of boys at Jones Elementary, mentioned in the premise
if boys_percentage_hypothesis >= boys_percentage_premise:
    # check if the estimate of 'boys_percentage_hypothesis' contradicts the percentage of boys in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
