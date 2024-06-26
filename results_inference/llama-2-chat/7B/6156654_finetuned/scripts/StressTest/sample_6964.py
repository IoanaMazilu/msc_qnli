property_size_last_year = 800
property_size_hypothesis = 700
price_last_year = 1000

# the hypothesis refers to the same locality and the same price range as the premise
if property_size_last_year!= property_size_hypothesis:
    # the hypothesis mentions a different property size than the premise, which contradicts the premise
    label = "contradiction"
elif price_last_year!= 1000:
    # the hypothesis mentions a different price than the premise, which contradicts the premise
    label = "contradiction"
else:
    # the hypothesis does not contradict the premise
    label = "neutral"

print(label)
