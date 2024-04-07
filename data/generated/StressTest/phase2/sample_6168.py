# Premise: Addison High School’s senior class has 200 boys and 160 girls.
# Hypothesis: Addison High School’s senior class has less than 400 boys and 160 girls.
# Golden Label: entailment

boys_premise = 200
boys_hypothesis = 400
girls_premise = 160
girls_hypothesis = 160

# the hypothesis refers to the number of boys and girls in the senior class mentioned in the premise
if boys_premise >= boys_hypothesis:
    # check if the number of boys in the premise contradicts the estimate of less than 'boys_hypothesis'
    label = "contradiction"
elif girls_premise != girls_hypothesis:
    # check if the number of girls in the hypothesis contradicts the number of girls reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

