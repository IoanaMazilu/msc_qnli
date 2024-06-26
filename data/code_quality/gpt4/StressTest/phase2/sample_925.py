echina_radius_premise = 1
echina_radius_hypothesis = 7

# the hypothesis talks about the radius of an echina, referenced also in the premise
if echina_radius_hypothesis <= echina_radius_premise:
    # check if the hypothesis value contradicts the estimate of more than 'echina_radius_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the radius of the echina
    # any radius greater than 'echina_radius_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
