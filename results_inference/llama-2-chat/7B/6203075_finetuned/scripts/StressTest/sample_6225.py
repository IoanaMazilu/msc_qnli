boys_premise = 300
boys_hypothesis = 400
girls_premise = 240
girls_hypothesis = 240

# the hypothesis refers to the number of boys and girls in Addison High School's senior class, as mentioned in the premise
if boys_premise >= boys_hypothesis:
    # check if the number of boys in the premise contradicts the hypothesis
    label = "contradiction"
elif girls_premise!= girls_hypothesis:
    # check if the number of girls in the premise contradicts the hypothesis
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
