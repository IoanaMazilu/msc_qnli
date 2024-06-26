pet_fish_premise = 26.0
pet_fish_eaten_premise = 6.0
current_pet_fish_hypothesis = 20.0

# compute the current number of pet fish after the cat ate some
current_pet_fish_premise = pet_fish_premise - pet_fish_eaten_premise

if current_pet_fish_hypothesis > current_pet_fish_premise:
    # check if the hypothesis value is greater than the current number of pet fish in the premise
    label = "entailment"
elif current_pet_fish_hypothesis < current_pet_fish_premise:
    # check if the hypothesis value is less than the current number of pet fish in the premise
    label = "contradiction"
else:
    # if the hypothesis value is equal to the current number of pet fish in the premise, there is no contradiction or entailment
    label = "neutral"

print(label)
