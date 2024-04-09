boys_premise = 200
girls_premise = 160

# the hypothesis refers to the number of boys and girls in the senior class
if boys_premise + girls_premise <= 400:
    # check if the hypothesis value contradicts the total number of students in the premise
    label = "contradiction"
elif boys_premise!= boys_premise_hypothesis or girls_premise!= girls_premise_hypothesis:
    # check if the number of boys or girls in the hypothesis contradicts the number of students in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
