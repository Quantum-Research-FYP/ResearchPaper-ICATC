OPENQASM 3.0;
include "stdgates.inc";
qubit[6] q;
rz(pi/2) q[0];
sx q[0];
rz(pi/2) q[0];
x q[1];
