# Premise: 1,250 people visited the zoo on Friday and 3 times as many people visited on Friday than on Saturday.
# Hypothesis: 413.7 people visited the zoo on Saturday.
# Golden Label: contradiction

people_friday_premise = 1250
people_saturday_hypothesis = 413.7

# the hypothesis refers to the number of people who visited on Saturday, which is also referenced in the premise
# compute the number of people who visited on Saturday in the premise
people_saturday_premise = people_friday_premise / 3
if people_saturday_hypothesis != people_saturday_premise:
    # check if the number of people who visited on Saturday in the hypothesis contradicts the number from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

