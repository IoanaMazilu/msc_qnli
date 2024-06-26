boys_premise = 200
boys_hypothesis = 700
girls_premise = 160
girls_hypothesis = 160

# the hypothesis refers to the number of boys and girls in the senior class mentioned in the premise
if boys_hypothesis!= boys_premise:
    # check if the number of boys in the hypothesis contradicts the number of boys reported in the premise
    label = "contradiction"
elif girls_hypothesis!= girls_premise:
    # check if the number of girls in the hypothesis contradicts the number of girls reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
