england_travelers_premise = 30
france_travelers_premise = 26
italy_travelers_premise = 32

less_than_70_england_hypothesis = 70
less_than_70_france_hypothesis = 26
less_than_70_italy_hypothesis = 32

# the hypothesis refers to the number of travelers to England, France, and Italy
# the hypothesis values are less than 70, which contradicts the premise values
# the premise does not entail the hypothesis

if england_travelers_premise > less_than_70_england_hypothesis:
    label = "contradiction"
elif france_travelers_premise!= less_than_70_france_hypothesis:
    label = "contradiction"
elif italy_travelers_premise!= less_than_70_italy_hypothesis:
    label = "contradiction"
else:
    label = "neutral"

print(label)
