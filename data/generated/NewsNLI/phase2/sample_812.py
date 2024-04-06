# Premise: Deforestation, which clears the way for food to be grown, accounts for 18 percent of the food and agriculture sector's emissions.
# Hypothesis: Food and Agricultural sector contribute over 33 percent of global emissions.
# Golden Label: neutral

emissions_food_agri_sector_premise = 0.18
emissions_food_agri_sector_hypothesis = 0.33

# the hypothesis mentions the percentage of global emissions contributed by the food and agriculture sector, which is also referenced in the premise
if emissions_food_agri_sector_hypothesis > emissions_food_agri_sector_premise:
    # check if the percentage mentioned in the hypothesis is greater than the percentage mentioned in the premise
    label = "contradiction"
else:
    # if the percentage from the hypothesis is not greater than the percentage in the premise, we can infer neutrality
    label = "neutral"

print(label)

