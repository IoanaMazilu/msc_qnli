# define variables for the numerical entities in the premise
pastor_position_premise = 9
pastor_relegation_premise = 10

# define variables for the numerical entities in the hypothesis
pastor_relegation_hypothesis = 10

# check if the relegation in the hypothesis contradicts the relegation in the premise
if pastor_relegation_hypothesis!= pastor_relegation_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
