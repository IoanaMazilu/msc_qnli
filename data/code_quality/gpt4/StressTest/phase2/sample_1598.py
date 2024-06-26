boys_premise = 160
boys_hypothesis = 760
girls_premise = 200
girls_hypothesis = 200

# the hypothesis states the number of boys and girls in Addison High School's senior class
if boys_premise != boys_hypothesis:
    # check if the number of boys in the hypothesis contradicts the number of boys in the premise
    label = "contradiction"
elif girls_premise != girls_hypothesis:
    # check if the number of girls in the hypothesis contradicts the number of girls in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
