# Premise: Japan's Current Account Surplus Adds 0.93 JPY Trillion In June Of 2017 To The Economy.
# Hypothesis: South Korea's Current Account Surplus Added USD 7.01 Billion In June Of 2017 To The Economy.
# Golden Label: neutral

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

