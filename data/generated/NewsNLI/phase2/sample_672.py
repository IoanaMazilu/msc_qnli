# Premise: The eastward moving storm dropped snow earlier across the Midwest and western Pennsylvania, with 9 inches reported in Urbana, Illinois, and 3.9 inches at O'Hare Airport outside Chicago.
# Hypothesis: O'Hare Airport gets 3.9 inches of snow, Detroit 5.5 inches.
# Golden Label: neutral

snow_urbana_premise = 9
snow_ohare_premise = 3.9
snow_ohare_hypothesis = 3.9
snow_detroit_hypothesis = 5.5

# the hypothesis mentions the snowfall at O'Hare Airport, which is also mentioned in the premise
# the hypothesis also mentions the snowfall in Detroit, which is not mentioned in the premise
if snow_ohare_hypothesis != snow_ohare_premise:
    # check if the snowfall at O'Hare Airport in the hypothesis contradicts the snowfall reported at O'Hare Airport in the premise
    label = "contradiction"
else:
    # if the snowfall at O'Hare Airport in the hypothesis does not contradict the snowfall at O'Hare Airport in the premise,
    # but the snowfall in Detroit is not mentioned in the premise, we can infer neutrality
    label = "neutral"

print(label)
