surplus_premise = 0.93
country_premise = "Japan"
year_premise = 2017

surplus_hypothesis = 7.01
country_hypothesis = "South Korea"
year_hypothesis = 2017

# the hypothesis and premise mention the current account surplus of two different countries in the same year
# however, the values of the surpluses and the countries are different, so we cannot infer entailment or contradiction
label = "neutral"

print(label)
