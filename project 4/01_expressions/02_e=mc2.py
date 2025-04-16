C = 299792458

def main():
    while True:
        mass_input = input("Enter kgs of mass (if you want to stop type 'exit' to quit): ")
        
        if mass_input.lower() == 'exit':
            print("Thank You!")
            break
        try:
            m = float(mass_input)
        except ValueError:
            print("Please enter a valid number.")
            continue

        energy = m * C ** 2

        print("\ne = m * C^2...\n")
        print("m =", m, "kg")
        print("C =", C, "m/s")
        print(f"{energy} joules of energy!\n")

main()
