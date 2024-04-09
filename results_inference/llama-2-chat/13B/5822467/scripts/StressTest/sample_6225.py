boys_premise = 300
girls_premise = 240

# define variables for the hypothesized values
boys_hypothesis = 200
girls_hypothesis = 240

# compare the number of boys in the premise and hypothesis
if boys_premise <= boys_hypothesis:
    # check if the estimate of 'boys_hypothesis' contradicts the number of boys in the premise
    label = "contradiction"
elif girls_hypothesis!= girls_premise:
    # check if the number of girls in the hypothesis contradicts the number of girls reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
