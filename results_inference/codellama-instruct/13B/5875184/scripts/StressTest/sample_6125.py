premise_people = 60
premise_iceland = 35
premise_norway = 23

hypothesis_people = 40
hypothesis_iceland = 35
hypothesis_norway = 23

# the hypothesis refers to the number of people and the number of people who have visited Iceland and Norway
if hypothesis_people <= premise_people:
    # check if the hypothesis value contradicts the estimate of more than 'premise_people'
    label = "contradiction"
elif hypothesis_iceland!= premise_iceland or hypothesis_norway!= premise_norway:
    # check if the number of people who have visited Iceland and Norway in the hypothesis contradicts the number of people who have visited Iceland and Norway reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
