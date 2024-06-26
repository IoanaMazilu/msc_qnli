people_died_bombardment = 10
people_left_fear = 20

# the hypothesis refers to the number of people who left the village on account of fear, mentioned in the premise
if people_left_fear!= people_died_bombardment:
    # check if the number of people who left the village on account of fear in the hypothesis contradicts the number of people who died by bombardment in the premise
    label = "contradiction"
else:
    # the premise and hypothesis refer to the same number of people who left the village on account of fear
    label = "entailment"

print(label)
