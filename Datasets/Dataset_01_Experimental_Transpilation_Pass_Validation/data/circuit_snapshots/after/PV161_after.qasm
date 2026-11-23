OPENQASM 3.0;
include "stdgates.inc";
qubit[7] q;
rz(pi/2) q[1];
sx q[1];
rz(pi/2) q[1];
cx q[1], q[2];
cx q[1], q[0];
cx q[3], q[2];
