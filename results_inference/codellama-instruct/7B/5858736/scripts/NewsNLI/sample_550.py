# Define variables with representative names for the numerical entities in both inputs
nasa_camera_data = 4
cooke_estimate = 4000
full_moon_brightness = 5
fireball_brightness = 5

# Extract all quantities as valid numbers (integers or floats)
nasa_camera_data = float(nasa_camera_data)
cooke_estimate = float(cooke_estimate)
full_moon_brightness = float(full_moon_brightness)
fireball_brightness = float(fireball_brightness)

# Use brief comments to explain what comparison you do between the defined variables
if fireball_brightness!= full_moon_brightness:
    # Check if the fireball brightness in the hypothesis contradicts the full moon brightness in the premise
    label = "contradiction"
else:
    # If the fireball brightness in the hypothesis is the same as the full moon brightness in the premise, we can infer entailment
    label = "entailment"

print(label)
