people_friday_premise = 1250
times_more_friday_than_saturday_premise = 3
people_saturday_hypothesis = 416.666666667

# the hypothesis refers to the number of people who visited the zoo on Saturday, which is also mentioned in the premise
# compute the number of people who visited the zoo on Saturday in the premise
people_saturday_premise = people_friday_premise * times_more_friday_than_saturday_premise
if people_saturday_hypothesis!= people_saturday_premise:
    # check if the number of people who visited the zoo on Saturday in the hypothesis contradicts the number of people who visited the zoo on Saturday in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
