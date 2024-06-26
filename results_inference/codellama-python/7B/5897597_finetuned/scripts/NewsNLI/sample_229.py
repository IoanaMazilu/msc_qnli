police_officers_killed_premise = 1
demonstrators_killed_premise = 5
people_wounded_premise = 1000

killed_hypothesis = 6
people_wounded_hypothesis = 1000

# the hypothesis mentions the number of killed and wounded people, which are also mentioned in the premise
if police_officers_killed_premise + demonstrators_killed_premise < killed_hypothesis:
    # check if the total number of killed people in the hypothesis contradicts the total number of killed people in the premise
    label = "contradiction"
elif people_wounded_hypothesis!= people_wounded_premise:
    # check if the number of wounded people from the hypothesis contradicts the number of wounded people in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
