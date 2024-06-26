# define variables for the numerical entities in the premise and hypothesis
japan_ca_surplus_2017 = 0.93
south_korea_ca_surplus_2017 = 7.01

# check if the hypothesis value contradicts the premise value
if south_korea_ca_surplus_2017 < japan_ca_surplus_2017:
    label = "contradiction"
else:
    label = "neutral"

print(label)
