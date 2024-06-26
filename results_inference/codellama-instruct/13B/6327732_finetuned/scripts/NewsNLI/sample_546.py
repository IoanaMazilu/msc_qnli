# define variables for the numerical entities in the premise
pastor_maldonado_qualification = 9
pastor_maldonado_relegation = 10

# define variables for the numerical entities in the hypothesis
pastor_maldonado_relegation_hypothesis = 10

# check if the relegation in the hypothesis contradicts the relegation in the premise
if pastor_maldonado_relegation_hypothesis!= pastor_maldonado_relegation:
    label = "contradiction"
else:
    label = "neutral"

print(label)
