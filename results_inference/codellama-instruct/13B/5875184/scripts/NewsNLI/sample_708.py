premise = "Around 1,000 people accused of being witches in Gambia have been locked up in secret detention centers and forced to drink a dangerous hallucinogenic potion, according to human rights organization Amnesty International."
hypothesis = "Victims forced to drink dangerous hallucinogenic potion ; at least two have died."

# extract the numerical entities from the premise
num_accused = 1000
num_detention_centers = 1
num_potions = 1

# extract the numerical entities from the hypothesis
num_victims = 2

# compare the values
if num_victims > num_accused:
    # the hypothesis mentions more victims than the premise
    label = "contradiction"
elif num_detention_centers > 1:
    # the hypothesis mentions more detention centers than the premise
    label = "contradiction"
elif num_potions > 1:
    # the hypothesis mentions more potions than the premise
    label = "contradiction"
else:
    # the hypothesis does not contradict the premise
    label = "neutral"

print(label)
