def kg_to_joules(mass_kg):

    c = 3 * pow(10, 8)  

    energy_joules = mass_kg * pow(c, 2)
    return energy_joules

mass = 1
energy = kg_to_joules(mass)
print(f"{mass} kg of mass is equivalent to {energy} joules of energy.")