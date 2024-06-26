# define variables for the number of people in the rebel group and the amount of military experience and time served by Suarez and Cano
num_people_premise = 2
suarez_military_experience_premise = 10
suarez_time_served_premise = 5
cano_military_experience_premise = 5
cano_time_served_premise = 5

# define variables for the number of people in the rebel group and the amount of military experience and time served by Suarez and Cano
num_people_hypothesis = 2
suarez_military_experience_hypothesis = 10
suarez_time_served_hypothesis = 5
cano_military_experience_hypothesis = 5
cano_time_served_hypothesis = 5

# check if the number of people in the rebel group contradicts the premise
if num_people_hypothesis!= num_people_premise:
    label = "contradiction"
# check if the amount of military experience and time served by Suarez contradicts the premise
elif suarez_military_experience_hypothesis!= suarez_military_experience_premise or suarez_time_served_hypothesis!= suarez_time_served_premise:
    label = "contradiction"
# check if the amount of military experience and time served by Cano contradicts the premise
elif cano_military_experience_hypothesis!= cano_military_experience_premise or cano_time_served_hypothesis!= cano_time_served_premise:
    label = "contradiction"
# if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
else:
    label = "entailment"

print(label)
