people_friday_premise = 1250.0
times_more_people_saturday_premise = 3.0
people_saturday_hypothesis = 3750.0

# the hypothesis refers to the number of people visiting the zoo on Saturday, which is also calculated in the premise
# compute the number of people who visited the zoo on Saturday in the premise
people_saturday_premise = people_friday_premise * times_more_people_saturday_premise
if people_saturday_hypothesis != people_saturday_premise:
    # check if the number of people on Saturday in the hypothesis contradicts the number of people on Saturday from the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"  

print(label)
