premise = "The ratio between the number of sheep and the number of horses at the Stewart farm is more than 1 to 7, If each horse is fed 230 ounces of horse food per day and the farm needs a total 12,880 ounces of horse food per day, what is the number of sheep in the farm?"
hypothesis = "The ratio between the number of sheep and the number of horses at the Stewart farm is 6 to 7, If each horse is fed 230 ounces of horse food per day and the farm needs a total 12,880 ounces of horse food per day, what is the number of sheep in the farm?"

# extract the numerical entities from the premise and hypothesis
premise_num_sheep = 12880 / 230
premise_num_horses = 12880 / 230
hypothesis_num_sheep = 12880 / 230
hypothesis_num_horses = 12880 / 230

# compare the numerical entities
if premise_num_sheep > hypothesis_num_sheep:
    label = "contradiction"
elif premise_num_horses > hypothesis_num_horses:
    label = "contradiction"
else:
    label = "neutral"

print(label)
