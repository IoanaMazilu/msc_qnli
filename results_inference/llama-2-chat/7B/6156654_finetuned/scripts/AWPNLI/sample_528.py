girls_premise = 542.0
boys_premise = 387.0
more_girls_hypothesis = 155.0

# the hypothesis refers to the number of girls and boys in the school
# the hypothesis states that there are more girls than boys in the school
# compute the number of girls and boys in the hypothesis
girls_hypothesis = girls_premise + more_girls_hypothesis
boys_hypothesis = boys_premise

# check if the number of girls in the hypothesis contradicts the number of girls in the premise
if girls_hypothesis!= girls_premise:
    label = "contradiction"
elif boys_hypothesis!= boys_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
