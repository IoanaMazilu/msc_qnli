boys_premise = 300
girls_premise = 240
boys_hypothesis = 400
girls_hypothesis = 240

# the hypothesis talks about the number of boys and girls in Addison High School's senior class, which is also mentioned in the premise
if boys_hypothesis <= boys_premise:
    # check if the hypothesis value contradicts the estimate of 'boys_premise'
    label = "contradiction"
elif girls_hypothesis!= girls_premise:
    # check if the number of girls in the hypothesis contradicts the number of girls reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
