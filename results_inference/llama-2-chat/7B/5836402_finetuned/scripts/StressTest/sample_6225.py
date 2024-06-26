boys_senior_class_premise = 300
girls_senior_class_premise = 240
boys_senior_class_hypothesis = 400
girls_senior_class_hypothesis = 240

# the hypothesis refers to the number of boys and girls in Addison High School's senior class mentioned in the premise
if boys_senior_class_premise >= boys_senior_class_hypothesis:
    # check if the estimate of 'boys_senior_class_hypothesis' contradicts the number of boys in the premise
    label = "contradiction"
elif girls_senior_class_hypothesis!= girls_senior_class_premise:
    # check if the number of girls in the hypothesis contradicts the number of girls reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
