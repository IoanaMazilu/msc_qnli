year_premise = 2003
year_hypothesis = 6003

# the hypothesis refers to the gender equality at Jefferson High School, mentioned also in the premise, but in a different year
if year_premise != year_hypothesis:
    # since the premise and hypothesis refer to different years, we can't infer if the gender balance remained the same over time
    label = "neutral"

print(label)
