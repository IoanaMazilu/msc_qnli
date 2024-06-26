people_with_hiv_aids_premise = 500000
people_with_hiv_aids_hypothesis = 430000

# the hypothesis mentions the number of people living with HIV/AIDS in China, which is also referenced in the premise
# however, the hypothesis refers to a specific legal protection, which cannot be entailed from the premise
if people_with_hiv_aids_hypothesis > people_with_hiv_aids_premise:
    # check if the number of people with HIV/AIDS in the hypothesis contradicts the number stated in the premise
    label = "contradiction"
else:
    # if the number of people with HIV/AIDS in the hypothesis is less than or equal to the number in the premise, it is neutral
    label = "neutral"

print(label)
