boys_percentage_premise = 80
boys_percentage_hypothesis = 10
girls_percentage_premise = 75
girls_percentage_hypothesis = 75

# the hypothesis refers to the percentage of boys and girls in the school mentioned in the premise
if boys_percentage_premise <= boys_percentage_hypothesis:
    # check if the estimate of 'boys_percentage_hypothesis' contradicts the percentage of boys in the premise
    label = "contradiction"
elif girls_percentage_hypothesis != girls_percentage_premise:
    # check if the percentage of girls in the hypothesis contradicts the percentage of girls reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
