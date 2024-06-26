premise = "If 1/12 of the passengers on a ship are from North America, 1/4 are Europeans, 2/9 are from Africa, 1/6 are from Asia and the remaining 50 people are citizens of other continents, then how many passengers are on board the ship?"
hypothesis = "If less than 7/12 of the passengers on a ship are from North America, 1/4 are Europeans, 2/9 are from Africa, 1/6 are from Asia and the remaining 50 people are citizens of other continents, then how many passengers are on board the ship?"

# extract the numerical entities from the premise and hypothesis
premise_entities = premise.split()
hypothesis_entities = hypothesis.split()

# define variables for the numerical entities
north_america = premise_entities[0]
europe = premise_entities[1]
africa = premise_entities[2]
asia = premise_entities[3]
other_continents = premise_entities[4]

# define variables for the numerical entities in the hypothesis
less_than_7_north_america = hypothesis_entities[0]

# check if the hypothesis value contradicts the premise value
if less_than_7_north_america <= north_america:
    label = "contradiction"
else:
    label = "neutral"

print(label)
