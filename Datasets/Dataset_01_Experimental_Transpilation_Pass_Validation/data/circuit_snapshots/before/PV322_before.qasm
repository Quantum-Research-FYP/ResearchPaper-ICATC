OPENQASM 3.0;
include "stdgates.inc";
qubit[3] q;
qubit[3] ancilla;
h q[0];
cx q[0], q[1];
cx q[1], q[2];
