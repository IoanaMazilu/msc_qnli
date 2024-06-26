friends_premise = 9.0
joined_people_premise = 7.0
wings_per_person_premise = 4.0
total_wings_hypothesis = 62.0

# the hypothesis refers to the total number of wings consumed which is also mentioned in the premise
# compute the total number of people and then the total number of wings consumed in the premise
total_people_premise = friends_premise + joined_people_premise
total_wings_premise = total_people_premise * wings_per_person_premise

if total_wings_hypothesis != total_wings_premise:
    # check if the total number of wings in the hypothesis contradicts the total number of wings from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
