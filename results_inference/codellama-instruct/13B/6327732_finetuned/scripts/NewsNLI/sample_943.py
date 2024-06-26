# define variables for the entities in the premise
costume_cover_face = True
container_more_than_1_liter = True
bulky_clothes = True

# define variables for the entities in the hypothesis
deaths = 3
wounded = 260

# check if the hypothesis values contradict the premise values
if deaths > 3:
    # if the number of deaths in the hypothesis is greater than 3, we can infer contradiction
    label = "contradiction"
elif wounded > 260:
    # if the number of wounded in the hypothesis is greater than 260, we can infer contradiction
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer neutral
    label = "neutral"

print(label)
