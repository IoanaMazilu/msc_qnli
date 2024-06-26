num_girls_premise = 542.0
num_boys_premise = 387.0
num_girls_hypothesis = 155.0

# the hypothesis refers to the number of girls and boys, which are also mentioned in the premise
# compute the total number of girls and boys in the premise
total_num_girls_premise = num_girls_premise + num_girls_hypothesis
total_num_boys_premise = num_boys_premise + num_girls_hypothesis
if total_num_girls_premise!= total_num_boys_premise:
    # check if the number of girls in the hypothesis contradicts the number of girls from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
