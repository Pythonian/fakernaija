from Faker9ja.faker import Faker

naija = Faker()

# Test the full_name() method
print("Random Full Name:", naija.full_name())
print("Random Ijaw Full Name:", naija.full_name(tribe="ijaw"))

# Test the male_full_name() method
print("Random Male Full Name:", naija.male_full_name())
print("Random Igbo Male Full Name:", naija.male_full_name(tribe="igbo"))

# Test the female_full_name() method
print("Random Female Full Name:", naija.female_full_name())
print("Random Edo Female Full Name:", naija.female_full_name(tribe="edo"))

# Test the first_name() method
print("Random First Name:", naija.first_name())
print("Random Yoruba First Name:", naija.first_name(tribe="yoruba"))

# Test the last_name() method
print("Random Last Name:", naija.last_name())
print("Random Fulani Last Name:", naija.last_name(tribe="fulani"))

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

print()

# Get a random school name
random_school_name = naija.school()
print("Random school name:", random_school_name)

# Get a random school acronym
random_school_acronym = naija.school(acronym=True)
print("Random school acronym:", random_school_acronym)

# Get a random school name at a specific location (e.g., Lagos)
random_school_name_in_lagos = naija.school(location="Lagos")
print("Random school name in Lagos:", random_school_name_in_lagos)

# Get a random school acronym at a specific location (e.g., Lagos)
random_school_acronym_in_lagos = naija.school(acronym=True, location="Lagos")
print("Random school acronym in Lagos:", random_school_acronym_in_lagos)

# Get a random federal school name
random_federal_school_name = naija.federal_school()
print("Random federal school name:", random_federal_school_name)

# Get a random federal school acronym
random_federal_school_acronym = naija.federal_school(acronym=True)
print("Random federal school acronym:", random_federal_school_acronym)

#  Get a random federal school name at a specific location
random_federal_school_name = naija.federal_school(location="Lagos")
print("Random federal school name in Lagos:", random_federal_school_name)

# Get a random federal school acronym at a specific location
federal_school_acronym = naija.federal_school(acronym=True, location="Lagos")
print("Random federal school acronym in Lagos:", federal_school_acronym)

# Get a random state school name
random_state_school_name = naija.state_school()
print("Random state school name:", random_state_school_name)

# Get a random state school acronym
random_state_school_acronym = naija.state_school(acronym=True)
print("Random state school acronym:", random_state_school_acronym)

#  Get a random state school name at a specific location
random_state_school_name = naija.state_school(location="Lagos")
print("Random state school name in Lagos:", random_state_school_name)

# Get a random state school acronym at a specific location
state_school_acronym = naija.state_school(acronym=True, location="Lagos")
print("Random state school acronym in Lagos:", state_school_acronym)

# Get a random private school name
random_private_school_name = naija.private_school()
print("Random private school name:", random_private_school_name)

# Get a random private school acronym
random_private_school_acronym = naija.private_school(acronym=True)
print("Random private school acronym:", random_private_school_acronym)

#  Get a random private school name at a specific location
random_private_school_name = naija.private_school(location="Lagos")
print("Random private school name in Lagos:", random_private_school_name)

# Get a random private school acronym at a specific location
private_school_acronym = naija.private_school(acronym=True, location="Lagos")
print("Random private school acronym in Lagos:", private_school_acronym)

# Get a random university name
random_university_school_name = naija.university()
print("Random university school name:", random_university_school_name)

# Get a random university acronym
random_university_acronym = naija.university(acronym=True)
print("Random university acronym:", random_university_acronym)

#  Get a random university name at a specific location
random_university_name = naija.university(location="Lagos")
print("Random university name in Lagos:", random_university_name)

# Get a random university acronym at a specific location
university_acronym = naija.university(acronym=True, location="Lagos")
print("Random university acronym in Lagos:", university_acronym)

# Get a random polytechnic name
random_polytechnic_school_name = naija.polytechnic()
print("Random polytechnic school name:", random_polytechnic_school_name)

# Get a random polytechnic acronym
random_polytechnic_acronym = naija.polytechnic(acronym=True)
print("Random polytechnic acronym:", random_polytechnic_acronym)

#  Get a random polytechnic name at a specific location
random_polytechnic_name = naija.polytechnic(location="Lagos")
print("Random polytechnic name in Lagos:", random_polytechnic_name)

# Get a random polytechnic acronym at a specific location
polytechnic_acronym = naija.polytechnic(acronym=True, location="Lagos")
print("Random polytechnic acronym in Lagos:", polytechnic_acronym)

# Get a random college_of_education name
random_college_of_education = naija.college_of_education()
print("Random college of education name:", random_college_of_education)

# Get a random college_of_education acronym
random_col_of_ed_acronym = naija.college_of_education(acronym=True)
print("Random college of education acronym:", random_col_of_ed_acronym)

#  Get a random college_of_education name at a specific location
random_col_of_ed_location = naija.college_of_education(location="Lagos")
print("Random college of education in Lagos:", random_col_of_ed_location)

# Get a random college_of_education acronym at a specific location
col_of_edu_acronym = naija.college_of_education(acronym=True, location="Lagos")
print("Random college of education acronym in Lagos:", col_of_edu_acronym)

# Random federal university name
random_federal_university_name = naija.federal_university()
print("Random Federal University Name:", random_federal_university_name)

# Random federal university acronym
random_federal_university_acronym = naija.federal_university(acronym=True)
print("Random Federal University Acronym:", random_federal_university_acronym)

# Random federal university in Lagos
random_federal_uni_in_lagos = naija.federal_university(location="Lagos")
print("Random Federal University in Lagos:", random_federal_uni_in_lagos)

# Random federal university acronym in Lagos
random_fed_acronym = naija.federal_university(acronym=True, location="Lagos")
print("Random Federal University Acronym in Lagos:", random_fed_acronym)

# Random federal polytechnic name
random_federal_polytechnic_name = naija.federal_polytechnic()
print("Random Federal polytechnic Name:", random_federal_polytechnic_name)

# Random federal polytechnic acronym
random_federal_poly_acronym = naija.federal_polytechnic(acronym=True)
print("Random Federal polytechnic Acronym:", random_federal_poly_acronym)

# Random federal polytechnic in Lagos
random_federal_uni_in_lagos = naija.federal_polytechnic(location="Lagos")
print("Random Federal polytechnic in Lagos:", random_federal_uni_in_lagos)

# Random federal polytechnic acronym in Lagos
random_fed_acronym = naija.federal_polytechnic(acronym=True, location="Lagos")
print("Random Federal polytechnic Acronym in Lagos:", random_fed_acronym)

# Random federal colofedu name
random_federal_colofedu = naija.federal_college_of_education()
print("Random Federal College of Education:", random_federal_colofedu)

# Random federal colofedu acronym
random_fedcoledu_acronym = naija.federal_college_of_education(acronym=True)
print("Random Federal College of Education Acronym:", random_fedcoledu_acronym)

# Random federal college of education in Lagos
random_fedcoledu_lagos = naija.federal_college_of_education(location="Lagos")
print("Random Federal College of Education in Lagos:", random_fedcoledu_lagos)

# Random federal college of education acronym in Lagos
random_fed_acronym = naija.federal_college_of_education(acronym=True, location="Lagos")
print("Random Federal College of Education acronym in Lagos:", random_fed_acronym)

# Random state university name
random_state_university_name = naija.state_university()
print("Random state university Name:", random_state_university_name)

# Random state university acronym
random_state_university_acronym = naija.state_university(acronym=True)
print("Random state university Acronym:", random_state_university_acronym)

# Random state university in Lagos
random_state_uni_in_lagos = naija.state_university(location="Lagos")
print("Random state university in Lagos:", random_state_uni_in_lagos)

# Random state university acronym in Lagos
random_fed_acronym = naija.state_university(acronym=True, location="Lagos")
print("Random state University Acronym in Lagos:", random_fed_acronym)

# Random state polytechnic name
random_state_polytechnic_name = naija.state_polytechnic()
print("Random state polytechnic Name:", random_state_polytechnic_name)

# Random state polytechnic acronym
random_state_polytechnic_acronym = naija.state_polytechnic(acronym=True)
print("Random state polytechnic Acronym:", random_state_polytechnic_acronym)

# Random state polytechnic in Lagos
random_state_uni_in_lagos = naija.state_polytechnic(location="Lagos")
print("Random state polytechnic in Lagos:", random_state_uni_in_lagos)

# Random state polytechnic acronym in Lagos
random_fed_acronym = naija.state_polytechnic(acronym=True, location="Lagos")
print("Random state polytechnic Acronym in Lagos:", random_fed_acronym)

# Random state college of education name
random_state_colofedu_name = naija.state_college_of_education()
print("Random state college of education:", random_state_colofedu_name)

# Random state college of education acronym
random_state_colofedu = naija.state_college_of_education(acronym=True)
print("Random state college of education Acronym:", random_state_colofedu)

# Random state college of education in Lagos
state_colofedu_lagos = naija.state_college_of_education(location="Lagos")
print("Random state college of education in Lagos:", state_colofedu_lagos)

# Random state college of education acronym in Lagos
colofedu_acronym = naija.state_college_of_education(acronym=True, location="Lagos")
print("Random state college of education Acronym in Lagos:", colofedu_acronym)
