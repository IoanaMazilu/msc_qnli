# define variables for the entities in the premise
costume_cover_face = True
container_more_than_1_liter = True
bulky_clothes = True

# define variables for the entities in the hypothesis
deaths = 3
wounded = 260

# check if the entities in the hypothesis contradict the entities in the premise
if deaths!= 3:
    # check if the number of deaths from the hypothesis contradicts the number of deaths in the premise
    label = "contradiction"
elif wounded!= 260:
    # check if the number of wounded from the hypothesis contradicts the number of wounded in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
