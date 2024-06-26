alice_leaves_city_a_premise = 30
bob_leaves_city_a_premise = 30
alice_leaves_city_a_hypothesis = 60

if alice_leaves_city_a_hypothesis <= alice_leaves_city_a_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
