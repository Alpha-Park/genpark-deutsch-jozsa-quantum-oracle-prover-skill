from client import DeutschJozsaProver

def main():
    print("=== Deutsch-Jozsa Quantum Oracle Prover ===")
    prover = DeutschJozsaProver(num_qubits=4)

    # Constant function: f(x) = 1 for all x
    constant_oracle = [1] * 16
    res_const = prover.solve(constant_oracle)
    print("Constant Oracle Test:", res_const)
    assert res_const["classification"] == "constant"

    # Balanced function: f(x) = x % 2
    balanced_oracle = [x % 2 for x in range(16)]
    res_bal = prover.solve(balanced_oracle)
    print("Balanced Oracle Test:", res_bal)
    assert res_bal["classification"] == "balanced"

    print("Deutsch-Jozsa Quantum Oracle Prover verified successfully!")

if __name__ == "__main__":
    main()
