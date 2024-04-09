west_town_speed = 4
east_town_speed = 1

# define variables for the numerical entities in the premise and hypothesis
birds_premise = west_town_speed + east_town_speed
birds_hypothesis = west_town_speed + east_town_speed

# extract all quantities as valid numbers
birds_premise = int(birds_premise)
birds_hypothesis = int(birds_hypothesis)

# compare the variables
if birds_hypothesis <= birds_premise:
    # check if the hypothesis value contradicts the estimate of 'birds_premise'
    label = "contradiction"
elif birds_premise!= birds_hypothesis:
    # check if the number of birds in the hypothesis contradicts the number of birds reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
