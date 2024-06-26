boys_premise = 200
girls_premise = 160
boys_hypothesis = 700
girls_hypothesis = 160

# the hypothesis refers to the number of boys and girls in the senior class, which are also mentioned in the premise
if boys_hypothesis!= boys_premise or girls_hypothesis!= girls_premise:
    # check if the number of boys or girls in the hypothesis contradicts the number of boys and girls in the premise
    label = "contradiction"
else:
    # if the number of boys and girls in the hypothesis does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
