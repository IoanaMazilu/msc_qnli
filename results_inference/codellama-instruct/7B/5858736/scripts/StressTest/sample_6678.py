aswin_age = 30
sachin_age = 35
sumesh_age = 40

# the hypothesis talks about the sum of ages of Aswin, Sachin and Sumesh
if (aswin_age + sachin_age + sumesh_age) <= 43:
    # check if the estimate of '43' contradicts the sum of ages in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the sum of ages
    # any number of years greater than '43' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
