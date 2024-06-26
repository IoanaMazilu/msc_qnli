girls_premise = 3
girls_hypothesis = 2
boys_premise = 3
boys_hypothesis = 2

# the hypothesis refers to the number of girls and boys in the date
if girls_hypothesis <= girls_premise:
    # check if the estimate of 'girls_hypothesis' contradicts the number of girls reported in the premise
    label = "contradiction"
elif boys_hypothesis!= boys_premise:
    # check if the number of boys in the hypothesis contradicts the number of boys reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
