OPENQASM 3.0;
include "stdgates.inc";
qubit[2] q;
qubit[4] ancilla;
h q[0];
cx q[0], q[1];
