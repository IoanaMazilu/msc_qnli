# Premise: Addison High School’s senior class has 300 boys and 240 girls.
# Hypothesis: Addison High School’s senior class has more than 300 boys and 240 girls.
# Golden Label: contradiction

boys_premise = 300
boys_hypothesis = 300
girls_premise = 240
girls_hypothesis = 240

# the hypothesis talks about the number of boys and girls in a class, referenced also in the premise
if boys_hypothesis != boys_premise:
    # check if the hypothesis value contradicts the exact number of boys 'boys_premise'
    label = "contradiction"
elif girls_hypothesis != girls_premise:
    # check if the hypothesis value contradicts the exact number of girls 'girls_premise'
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

