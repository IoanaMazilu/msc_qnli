premise = "Jill, who lives in City C, plans to visit 7 different cities, M, L, P, I, Y, B and S."
hypothesis = "Jill, who lives in City C, plans to visit 6 different cities, M, L, P, I, Y, B and S."

# extract the number of cities mentioned in the premise
premise_cities = premise.split(",")[2].split(" ")[0]
# extract the number of cities mentioned in the hypothesis
hypothesis_cities = hypothesis.split(",")[2].split(" ")[0]

# check if the hypothesis value contradicts the premise value
if hypothesis_cities < premise_cities:
    label = "contradiction"
else:
    label = "neutral"

print(label)
