european_countries_premise = 14
world_population_premise = 5 / 100  # 5% converted to a decimal
population_growth_premise = 0
japan_population_growth_premise = 0
france_population_growth_premise = 0
finland_population_growth_premise = 0
japan_population_growth_hypothesis = 0

# the hypothesis talks about the population growth of Japan, which is also mentioned in the premise
if japan_population_growth_hypothesis != japan_population_growth_premise:
    # check if the population growth of Japan in the hypothesis contradicts the population growth from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
