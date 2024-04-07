# Premise: Addison High School’s senior class has 300 boys and 240 girls.
# Hypothesis: Addison High School’s senior class has less than 400 boys and 240 girls.
# Golden Label: entailment

boys_premise = 300
boys_hypothesis = 400
girls_premise = 240
girls_hypothesis = 240

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
