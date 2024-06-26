mpg_premise = 32
mpg_hypothesis = 32

# the hypothesis talks about the miles per gallon Dan's car gets, also mentioned in the premise
if mpg_hypothesis > mpg_premise:
    # check if the hypothesis value contradicts the exact mpg mentioned in the premise
    label = "contradiction"
elif mpg_hypothesis == mpg_premise:
    # if the mpg in the hypothesis is equal to the mpg in the premise, it's not more than the premise's mpg
    label = "contradiction"
else:
    # the premise gives the exact miles per gallon, the hypothesis can't entail more than the exact number
    label = "neutral"

print(label)
