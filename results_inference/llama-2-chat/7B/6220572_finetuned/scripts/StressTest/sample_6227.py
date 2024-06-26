boys_premise = 300
boys_hypothesis = 300
girls_premise = 240
girls_hypothesis = 240

# the hypothesis talks about the number of boys and girls in the senior class of Addison High School, referenced also in the premise
if boys_hypothesis!= boys_premise:
    # check if the number of boys in the hypothesis contradicts the number of boys reported in the premise
    label = "contradiction"
elif girls_hypothesis!= girls_premise:
    # check if the number of girls in the hypothesis contradicts the number of girls reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)