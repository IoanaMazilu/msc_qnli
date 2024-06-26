qualified_position_premise = 9
relegated_position_premise = 10
relegated_position_hypothesis = 10

# the hypothesis mentions the relegation of Maldonado, which is also referenced in the premise
# however, the hypothesis does not mention the initial position of Maldonado, which is mentioned in the premise
if relegated_position_hypothesis!= relegated_position_premise:
    # check if the relegation position in the hypothesis contradicts the relegation position reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer neutrality
    label = "neutral"

print(label)
