gerbil_count_premise = 96 // 2 # divide by 2 to get the number of gerbils
hamster_count_premise = 96 // 2 # divide by 2 to get the number of hamsters
total_pets_premise = gerbil_count_premise + hamster_count_premise

gerbil_count_hypothesis = int(56 / 2) # divide by 2 to get the number of gerbils
hamster_count_hypothesis = int(56 / 2) # divide by 2 to get the number of hamsters
total_pets_hypothesis = gerbil_count_hypothesis + hamster_count_hypothesis

# check if the hypothesis values and estimates do not contradict the premise ones
if total_pets_hypothesis > total_pets_premise:
    # check if the estimate of 'total_pets_hypothesis' contradicts the number of pets reported in the premise
    label = "contradiction"
elif gerbil_count_hypothesis!= gerbil_count_premise or hamster_count_hypothesis!= hamster_count_premise:
    # check if the number of gerbils or hamsters in the hypothesis contradicts the number of gerbils or hamsters reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
