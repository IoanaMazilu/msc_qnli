boys_senior_class_premise = 200
girls_senior_class_premise = 160
boys_senior_class_hypothesis = 700
girls_senior_class_hypothesis = 160

# the hypothesis refers to the number of boys and girls in Addison High School's senior class mentioned in the premise
if boys_senior_class_premise + girls_senior_class_premise!= girls_senior_class_hypothesis:
    # check if the number of girls in the hypothesis contradicts the number of girls reported in the premise
    label = "contradiction"
elif boys_senior_class_hypothesis!= boys_senior_class_premise:
    # check if the number of boys in the hypothesis contradicts the number of boys reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
