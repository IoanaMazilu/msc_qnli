# Premise: Addison High School’s senior class has less than 400 boys and 160 girls.
# Hypothesis: Addison High School’s senior class has 200 boys and 160 girls.
# Golden Label: neutral

boys_premise = 400
boys_hypothesis = 200
girls_premise = 160
girls_hypothesis = 160

# the hypothesis talks about the number of boys and girls in the senior class, referenced also in the premise
if boys_hypothesis >= boys_premise:
    # check if the number of boys in the hypothesis contradicts the estimate of less than 'boys_premise'
    label = "contradiction"
elif girls_hypothesis != girls_premise:
    # check if the number of girls in the hypothesis contradicts the number of girls reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of boys
    # any number of boys less than 'boys_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

