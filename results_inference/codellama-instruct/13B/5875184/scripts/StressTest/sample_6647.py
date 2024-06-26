premise = "If 1/12 of the passengers on a ship are from North America, 1/4 are Europeans, 2/9 are from Africa, 1/6 are from Asia and the remaining 50 people are citizens of other continents, then how many passengers are on board the ship?"
hypothesis = "If more than 1/12 of the passengers on a ship are from North America, 1/4 are Europeans, 2/9 are from Africa, 1/6 are from Asia and the remaining 50 people are citizens of other continents, then how many passengers are on board the ship?"

# extract the numerical entities from the premise and hypothesis
premise_entities = premise.split(" ")
hypothesis_entities = hypothesis.split(" ")

# define variables for the numerical entities
north_america = premise_entities[2]
europe = premise_entities[4]
africa = premise_entities[6]
asia = premise_entities[8]
other_continents = premise_entities[10]

# define variables for the hypothetical entities
more_north_america = hypothesis_entities[2]
more_europe = hypothesis_entities[4]
more_africa = hypothesis_entities[6]
more_asia = hypothesis_entities[8]
more_other_continents = hypothesis_entities[10]

# perform calculations
total_passengers = north_america + europe + africa + asia + other_continents
more_total_passengers = more_north_america + more_europe + more_africa + more_asia + more_other_continents

# compare the hypothetical and premise values
if more_total_passengers > total_passengers:
    label = "entailment"
elif more_total_passengers < total_passengers:
    label = "contradiction"
else:
    label = "neutral"

print(label)
