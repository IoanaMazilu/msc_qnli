girls_premise = 542.0
boys_premise = 387.0
more_girls_hypothesis = 155.0

# the hypothesis talks about the difference in number of girls and boys, which are also referenced in the premise
# compute the difference in number of girls and boys from the premise
difference_girls_boys_premise = girls_premise - boys_premise
if more_girls_hypothesis!= difference_girls_boys_premise:
    # check if the difference in girls and boys from the hypothesis contradicts the difference from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
