OPENQASM 3.0;
include "stdgates.inc";
qubit[7] q;
rz(pi/2) q[0];
sx q[0];
rz(-2.2415926535897936) q[0];
sx q[0];
rz(1.8707963267948955) q[0];
