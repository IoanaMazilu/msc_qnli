girls_premise = 2
girls_hypothesis = 6
boys_premise = 3
boys_hypothesis = 3

# the hypothesis refers to the number of girls and boys mentioned in the premise
if girls_hypothesis < girls_premise:
    # check if the number of girls in the hypothesis contradicts the number of girls in the premise
    label = "contradiction"
elif boys_hypothesis != boys_premise:
    # check if the number of boys in the hypothesis contradicts the number of boys in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
