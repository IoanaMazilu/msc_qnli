unique_meals_premise = 100
unique_meals_hypothesis = 100
countries_premise = 100
countries_hypothesis = 100

# the hypothesis mentions the plan to sample 100 meals in 100 countries, which is also referenced in the premise
# however, the premise refers to unique meals, while the hypothesis refers to weird and wonderful meals.
# the characteristics of these meals cannot be entailed from the premise
label = "neutral"

print(label)
