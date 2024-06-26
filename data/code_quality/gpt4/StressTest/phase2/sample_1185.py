girls_premise = 4
girls_hypothesis = 2
boys_premise = 4
boys_hypothesis = 4

# the hypothesis refers to the number of girls and boys mentioned in the premise
if girls_premise <= girls_hypothesis:
    # check if the estimate of 'girls_hypothesis' contradicts the number of girls in the premise
    label = "contradiction"
elif boys_hypothesis != boys_premise:
    # check if the number of boys in the hypothesis contradicts the number of boys reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
