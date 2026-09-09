import sys
import json
from client import DeutschJozsaProver

def handle_request(req):
    method = req.get("method")
    params = req.get("params", {})
    if method == "classify":
        qubits = params.get("num_qubits", 3)
        oracle = params.get("oracle", [0] * (1 << qubits))
        prover = DeutschJozsaProver(qubits)
        return prover.solve(oracle)
    return {"error": "Unknown method"}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        req = json.loads(line)
        res = handle_request(req)
        print(json.dumps(res))
        sys.stdout.flush()

if __name__ == "__main__":
    main()
