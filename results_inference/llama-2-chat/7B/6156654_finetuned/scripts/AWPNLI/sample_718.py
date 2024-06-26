visitors_friday = 1250
visitors_friday_per_saturday = 3
visitors_saturday = visitors_friday * visitors_friday_per_saturday

# the hypothesis refers to the number of visitors on Saturday, which can be calculated from the premise
# the hypothesis value is 416.666666667
if visitors_saturday == 416.666666667:
    # the hypothesis value is equal to the calculated value from the premise
    label = "entailment"
elif visitors_saturday!= visitors_friday:
    # the hypothesis value cannot be computed from the premise
    # the hypothesis value is a fraction, which cannot be computed from the premise
    label = "contradiction"
else:
    # the hypothesis value is a fraction, which cannot be computed from the premise
    # the hypothesis value is not equal to the calculated value from the premise
    label = "contradiction"

print(label)
