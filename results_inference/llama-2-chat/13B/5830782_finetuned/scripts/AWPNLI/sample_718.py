people_friday_premise = 1250
people_saturday_hypothesis = 416.666666667

# the hypothesis refers to the number of people who visited the zoo on Saturday, which is also mentioned in the premise
# compute the number of people who visited the zoo on Saturday according to the premise
people_saturday_premise = people_friday_premise / 3
if people_saturday_hypothesis!= people_saturday_premise:
    # check if the number of people who visited the zoo on Saturday in the hypothesis contradicts the number from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
