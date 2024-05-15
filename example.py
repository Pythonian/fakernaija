from Faker9ja.faker import Faker

naija = Faker()

# Test the full_name() method
print("Random Full Name:", naija.full_name())
print("Random Igbo Full Name:", naija.full_name(tribe="igbo"))

# Test the male_full_name() method
print("Random Male Full Name:", naija.male_full_name())
print("Random Igbo Male Full Name:", naija.male_full_name(tribe="igbo"))

# Test the female_full_name() method
print("Random Female Full Name:", naija.female_full_name())
print("Random Igbo Female Full Name:", naija.female_full_name(tribe="igbo"))

# Test the first_name() method
print("Random First Name:", naija.first_name())
print("Random Yoruba First Name:", naija.first_name(tribe="yoruba"))

# Test the last_name() method
print("Random Last Name:", naija.last_name())
print("Random Yoruba Last Name:", naija.last_name(tribe="yoruba"))

# Test the male_first_name() method
print("Random Male First Name:", naija.male_first_name())
print("Random Hausa Male First Name:", naija.male_first_name(tribe="hausa"))

# Test the female_first_name() method
print("Random Female First Name:", naija.female_first_name())
print("Random Hausa Female First Name:", naija.female_first_name(tribe="hausa"))

# Test the prefix() method
print("Random Name Prefix:", naija.prefix())

# Test the male_prefix() method
print("Random Male Name Prefix:", naija.male_prefix())

# Test the female_prefix() method
print("Random Female Name Prefix:", naija.female_prefix())

print()

# Get a random state
print("Random state:", naija.state())

# Get a random state shortcode
print("Random state shortcode:", naija.state(shortcode=True))

# Get a random state from a specific region
print("Random state by Region:", naija.state(region_initial="NC"))

# Get a random state capital
print("Random state capital:", naija.capital())

# Get a random Local Government Area (LGA)
print("Random LGA:", naija.lga())

# Get a random LGA in a specific state
print("Random LGA in Abia:", naija.lga(state="Abia"))

# Get a random geopolitical region
print("Random region:", naija.region())

# Get a random geopolitical region by initial
print("Get random region by initial:", naija.region(initial=True))

# Get a random postal code of any state
print("Random postal code:", naija.postal_code())

# Get the postal code of a specific state (e.g., Lagos)
print("Postal code of Lagos:", naija.postal_code(state="Lagos"))
