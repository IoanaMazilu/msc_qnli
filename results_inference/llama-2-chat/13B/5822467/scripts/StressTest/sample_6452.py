# Define variables with representative names for the numerical entities in both inputs
north_america_premise = 1/12
europe_premise = 1/4
africa_premise = 1/9
asia_premise = 1/6
other_continents_premise = 42

# Extract all quantities as valid numbers (integers or floats)
north_america_hypothesis = float(input("Enter a fraction of passengers from North America: "))
europe_hypothesis = float(input("Enter a fraction of passengers from Europe: "))
africa_hypothesis = float(input("Enter a fraction of passengers from Africa: "))
asia_hypothesis = float(input("Enter a fraction of passengers from Asia: "))
other_continents_hypothesis = float(input("Enter a fraction of passengers from other continents: "))

# Use brief comments to explain what comparison we do between the defined variables
# (do not use their values in the comments)

# Compare the number of passengers from North America in the premise and hypothesis
if north_america_hypothesis < north_america_premise:
    # Check if the hypothesis value contradicts the estimate of 'north_america_premise'
    label = "contradiction"
elif north_america_hypothesis > north_america_premise:
    # Check if the hypothesis value entails the estimate of 'north_america_premise'
    label = "entailment"
else:
    # The hypothesis value is neutral with respect to the premise
    label = "neutral"

# Compare the number of passengers from Europe in the premise and hypothesis
if europe_hypothesis < europe_premise:
    # Check if the hypothesis value contradicts the estimate of 'europe_premise'
    label = "contradiction"
elif europe_hypothesis > europe_premise:
    # Check if the hypothesis value entails the estimate of 'europe_premise'
    label = "entailment"
else:
    # The hypothesis value is neutral with respect to the premise
    label = "neutral"

# Compare the number of passengers from Africa in the premise and hypothesis
if africa_hypothesis < africa_premise:
    # Check if the hypothesis value contradicts the estimate of 'africa_premise'
    label = "contradiction"
elif africa_hypothesis > africa_premise:
    # Check if the hypothesis value entails the estimate of 'africa_premise'
    label = "entailment"
else:
    # The hypothesis value is neutral with respect to the premise
    label = "neutral"

# Compare the number of passengers from Asia in the premise and hypothesis
if asia_hypothesis < asia_premise:
    # Check if the hypothesis value contradicts the estimate of 'asia_premise'
    label = "contradiction"
elif asia_hypothesis > asia_premise:
    # Check if the hypothesis value entails the estimate of 'asia_premise'
    label = "entailment"
else:
    # The hypothesis value is neutral with respect to the premise
    label = "neutral"

# Compare the number of passengers from other continents in the premise and hypothesis
if other_continents_hypothesis < other_continents_premise:
    # Check if the hypothesis value contradicts the estimate of 'other_continents_premise'
    label = "contradiction"
elif other_continents_hypothesis > other_continents_premise:
    # Check if the hypothesis value entails the estimate of 'other_continents_premise'
    label = "entailment"
else:
    # The hypothesis value is neutral with respect to the premise
    label = "neutral"

print(label)
