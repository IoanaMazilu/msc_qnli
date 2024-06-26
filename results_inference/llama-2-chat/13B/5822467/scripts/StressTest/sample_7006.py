gerbil_count_premise = 56
gerbil_count_hypothesis = 96
hamster_count_premise = 56
hamster_count_hypothesis = 96

# the hypothesis refers to the total number of pets, which is a combination of gerbils and hamsters
if gerbil_count_premise + hamster_count_premise <= gerbil_count_hypothesis + hamster_count_hypothesis:
    # check if the estimate of 'gerbil_count_hypothesis' and 'hamster_count_hypothesis' contradicts the premise
    label = "contradiction"
elif gerbil_count_premise!= gerbil_count_hypothesis or hamster_count_premise!= hamster_count_hypothesis:
    # check if the number of gerbils or hamsters in the hypothesis contradicts the number of gerbils or hamsters reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
