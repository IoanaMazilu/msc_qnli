countries_premise = 3
countries_hypothesis = 2
launch_year_premise = 1999
adoption_year_hypothesis = 1999

# the hypothesis talks about Sweden adopting the euro currency in a certain year, which is not mentioned in the premise
# the premise only mentions Denmark, Sweden, and Britain deciding not to join the euro currency system in 1999
# we cannot infer from the premise that Sweden adopted the euro currency in 1999
label = "neutral"

print(label)
