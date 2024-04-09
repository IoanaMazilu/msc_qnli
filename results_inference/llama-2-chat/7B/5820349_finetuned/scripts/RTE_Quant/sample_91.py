hiv_people_premise = 39.4e6
hiv_people_hypothesis = 39.4e6

# the hypothesis talks about the number of people living with HIV, which is also mentioned in the premise
if hiv_people_hypothesis!= hiv_people_premise:
    # check if the number of people living with HIV in the hypothesis contradicts the number of people from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
