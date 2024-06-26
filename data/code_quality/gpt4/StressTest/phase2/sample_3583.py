more_supermarkets_us_premise = 54
more_supermarkets_us_hypothesis = 14

# the hypothesis refers to the number of FGH supermarkets in the US compared to Canada mentioned in the premise
if more_supermarkets_us_hypothesis >= more_supermarkets_us_premise:
    # check if the hypothesis value contradicts the premise's statement of less than 'more_supermarkets_us_premise'
    label = "contradiction"
elif more_supermarkets_us_hypothesis < more_supermarkets_us_premise:
    # if the hypothesis value is less than the premise value, it is consistent with the premise
    # but because the premise gives only an upper limit, we can't infer the exact number from it
    label = "neutral"

print(label)
