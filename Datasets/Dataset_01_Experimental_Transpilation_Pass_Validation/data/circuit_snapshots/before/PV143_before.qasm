OPENQASM 3.0;
include "stdgates.inc";
qubit[6] q;
h q[0];
barrier q[0];
h q[0];
barrier q[0];
h q[0];
