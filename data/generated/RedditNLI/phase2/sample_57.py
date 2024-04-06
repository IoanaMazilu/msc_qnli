# Premise: 40% Of Venezuela Stores Go Bust After 3,000% Minimum Wage Hike.
# Hypothesis: In Venezuela, Huge Hike in Minimum Wage Forces 40 Percent of Stores to Close.
# Golden Label: entailment

percentage_stores_premise = 40
percentage_stores_hypothesis = 40
wage_hike_premise = 3000
# the wage hike in the hypothesis is not quantified, so we can't compare it to the premise

# the hypothesis and premise mention the percentage of stores that go bust after a minimum wage hike
if percentage_stores_premise != percentage_stores_hypothesis:
    # check if the percentage of stores in the hypothesis contradicts the percentage in the premise
    label = "contradiction"
else:
    # if the values in the hypothesis do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

