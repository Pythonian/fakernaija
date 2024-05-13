from Faker9ja.faker import NameGenerator

# Create instances of provider classes and use them as needed
faker = NameGenerator()

print("Random Hausa names:")
for i in range(5):
    full_name = faker.full_name("hausa")
    print(full_name)
print()

print("Random Yoruba male names:")
for i in range(5):
    full_name = faker.full_name(ethnic_group="yoruba", gender="male")
    print(full_name)
print()

print("Random Igbo female names:")
for i in range(5):
    full_name = faker.full_name(ethnic_group="igbo", gender="female")
    print(full_name)
print()

print("Random Yoruba female first names:")
for i in range(5):
    first_name = faker.first_name(ethnic_group="yoruba", gender="female")
    print(first_name)
print()

print("Random Igbo last names:")
for i in range(5):
    last_name = faker.last_name("igbo")
    print(last_name)
