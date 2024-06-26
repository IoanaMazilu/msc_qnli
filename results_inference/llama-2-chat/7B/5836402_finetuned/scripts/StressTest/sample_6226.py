boys_premise = 400
boys_hypothesis = 300
girls_premise = 240
girls_hypothesis = 240

# the hypothesis refers to the number of boys and girls in Addison High School's senior class, which is also mentioned in the premise
if boys_hypothesis <= boys_premise:
    # check if the estimate of 'boys_hypothesis' contradicts the number of boys in the premise
    label = "contradiction"
elif girls_hypothesis!= girls_premise:
    # check if the number of girls in the hypothesis contradicts the number of girls reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
