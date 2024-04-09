boys_premise = 200
girls_premise = 160
boys_hypothesis = 399
girls_hypothesis = 160

# the hypothesis talks about the number of boys and girls in the senior class of Addison High School
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
