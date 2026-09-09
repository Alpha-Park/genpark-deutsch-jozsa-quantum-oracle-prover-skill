import math

class DeutschJozsaProver:
    """Exact single-query quantum evaluation distinguishing constant vs balanced functions."""
    def __init__(self, num_qubits: int):
        self.num_qubits = num_qubits
        self.total_inputs = 1 << num_qubits

    def solve(self, oracle_values: list[int]) -> dict:
        """
        oracle_values: list of 0 or 1 for each input x in range(2^num_qubits).
        """
        if len(oracle_values) != self.total_inputs:
            raise ValueError(f"Oracle must have {self.total_inputs} values.")

        # Simulate Walsh-Hadamard transform after oracle phase kickback
        # Amplitude of |0...0> is (1/2^n) * sum_x (-1)^f(x)
        phase_sum = sum((-1) ** f for f in oracle_values)
        zero_state_amplitude = phase_sum / self.total_inputs
        prob_all_zeros = abs(zero_state_amplitude) ** 2

        if abs(prob_all_zeros - 1.0) < 1e-6:
            classification = "constant"
            confidence = 1.0
        elif abs(prob_all_zeros) < 1e-6:
            classification = "balanced"
            confidence = 1.0
        else:
            classification = "neither (invalid oracle)"
            confidence = round(prob_all_zeros, 4)

        return {
            "num_qubits": self.num_qubits,
            "classification": classification,
            "prob_all_zeros": round(prob_all_zeros, 6),
            "quantum_queries": 1,
            "classical_deterministic_queries_needed": (self.total_inputs // 2) + 1
        }
