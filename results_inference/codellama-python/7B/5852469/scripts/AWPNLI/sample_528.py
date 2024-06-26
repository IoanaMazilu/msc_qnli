girls_premise = 542
boys_premise = 387
girls_hypothesis = 542
boys_hypothesis = 387

# the hypothesis refers to the number of girls and boys in the school
# compute the total number of girls and boys in the premise
total_girls_premise = girls_premise + boys_premise
total_boys_premise = total_girls_premise

# check if the total number of girls in the hypothesis contradicts the estimate of more than 'girls_premise'
if girls_hypothesis >= total_girls_premise:
    label = "contradiction"
elif boys_hypothesis >= total_boys_premise:
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
