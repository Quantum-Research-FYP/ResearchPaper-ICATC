OPENQASM 3.0;
include "stdgates.inc";
qubit[7] q;
h q[0];
barrier q[0], q[1];
cx q[0], q[1];
barrier q[0], q[1];
x q[1];
