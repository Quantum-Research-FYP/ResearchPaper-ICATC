OPENQASM 3.0;
include "stdgates.inc";
qubit[6] q;
h q[0];
h q[1];
cz q[0], q[1];
h q[0];
h q[1];
