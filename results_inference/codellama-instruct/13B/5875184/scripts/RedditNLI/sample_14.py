premise = "World oil demand will exceed supply in the second half of the year unless we can increase production by 1.5 million barrels a day."
hypothesis = "Oil markets facing shortfall in the second half (ie. demand will surpass supply unless we fond another 1.5 million barrels of oil a day)."

# extract the numerical entities from the premise and hypothesis
premise_production_increase = 1.5
hypothesis_production_increase = 1.5

# check if the production increase in the hypothesis contradicts the premise
if hypothesis_production_increase < premise_production_increase:
    label = "contradiction"
else:
    label = "neutral"

print(label)
