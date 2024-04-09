girl_names_premise = ["Rebecca", "Kate", "Ashley"]
boy_names_premise = ["Peter", "Kyle", "Sam"]
girl_names_hypothesis = ["Rebecca", "Kate", "Ashley", "more than 1"]
boy_names_hypothesis = ["Peter", "Kyle", "Sam"]

# the hypothesis talks about the number of girls and boys in a date, referenced also in the premise
if len(girl_names_hypothesis) <= len(girl_names_premise):
    # check if the number of girls in the hypothesis contradicts the number of girls in the premise
    label = "contradiction"
elif len(boy_names_hypothesis)!= len(boy_names_premise):
    # check if the number of boys in the hypothesis contradicts the number of boys in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of girls and boys
    # any number of girls and boys consistent with the premise is consistent with the hypothesis, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
