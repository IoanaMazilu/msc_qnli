boys_premise = 200
girls_premise = 160
boys_hypothesis = 400
girls_hypothesis = 160

# the hypothesis refers to the number of boys and girls in Addison High School's senior class
if boys_premise + girls_premise >= boys_hypothesis + girls_hypothesis:
    # check if the total number of boys and girls in the premise contradicts the hypothesis
    label = "contradiction"
elif boys_premise!= boys_hypothesis or girls_premise!= girls_hypothesis:
    # check if the number of boys or girls in the premise contradicts the hypothesis
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
