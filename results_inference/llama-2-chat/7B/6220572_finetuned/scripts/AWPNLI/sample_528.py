girls_premise = 542.0
boys_premise = 387.0
total_girls_boys_premise = girls_premise + boys_premise

# the hypothesis talks about the difference in the number of girls and boys
# compute the difference in the premise
difference_premise = total_girls_boys_premise - boys_premise

# check if the difference in the hypothesis contradicts the difference in the premise
if difference_hypothesis!= difference_premise:
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
