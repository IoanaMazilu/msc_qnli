boys_premise = 160
boys_hypothesis = 260
girls_premise = 200
girls_hypothesis = 200

# the hypothesis refers to the number of boys and girls in the senior class mentioned in the premise
if boys_premise >= boys_hypothesis:
    # check if the estimate of 'boys_hypothesis' contradicts the number of boys in the premise
    label = "contradiction"
elif girls_premise != girls_hypothesis:
    # check if the number of girls in the hypothesis contradicts the number of girls reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
