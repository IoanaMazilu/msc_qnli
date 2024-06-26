boys_premise = 300
girls_premise = 240
boys_hypothesis = 400
girls_hypothesis = 240

# the hypothesis refers to the number of boys and girls in the senior class, which is also mentioned in the premise
if boys_premise >= boys_hypothesis or girls_premise >= girls_hypothesis:
    # check if the number of boys or girls in the hypothesis contradicts the number of boys or girls in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
