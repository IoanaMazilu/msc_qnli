# Premise: Addison High School’s senior class has less than 260 boys and 200 girls.
# Hypothesis: Addison High School’s senior class has 160 boys and 200 girls.
# Golden Label: neutral

boys_premise = 260
boys_hypothesis = 160
girls_premise = 200
girls_hypothesis = 200

# the hypothesis talks about the number of boys and girls in Addison High School's senior class, mentioned in the premise
if boys_hypothesis >= boys_premise:
    # check if the number of boys in the hypothesis contradicts the estimate of less than 'boys_premise' boys
    label = "contradiction"
elif girls_hypothesis != girls_premise:
    # check if the number of girls in the hypothesis contradicts the number of girls reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of boys, and an exact number for the girls
    # any number of boys less than 'boys_premise' and 'girls_premise' girls is consistent with the premise and can be explicitly entailed from the premise
    label = "entailment"

print(label)

