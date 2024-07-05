from nada_dsl import *

def nada_main():
    # Define parties involved in the computation
    party1 = Party(name="Party1")
    party2 = Party(name="Party2")
    party3 = Party(name="Party3")

    # Securely input integers from respective parties
    input_a = SecretInteger(Input(name="A", party=party1))
    input_b = SecretInteger(Input(name="B", party=party2))

    # Perform secure addition of the two secret inputs
    result = input_a + input_b

    # Output the result to the designated party
    output = Output(result, name="my_output", party=party3)

    return [output]

# Entry point of the nada program
if __name__ == "__main__":
    try:
        # Run the main function and retrieve the output
        outputs = nada_main()
        for output in outputs:
            print(f"Output {output.name} for party {output.party.name}: {output.value}")
    except Exception as e:
        print(f"An error occurred: {e}")
        # Handle the error or clean up as necessary
