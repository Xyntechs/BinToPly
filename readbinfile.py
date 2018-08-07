import numpy as np

redF = np.fromfile("inp1.bin", dtype=float, count=-1, sep='')
redF=redF.astype(int)
redF=redF[np.nonzero(redF)]
print(len(redF))
rows =len(redF)/3; #divide the points on X Y Z  
with open("inp1.ply","w") as f:
	f.write("ply\nformat ascii 1.0\nelement vertex %d\nproperty float32 x\nproperty float32 y\nproperty float32 z\nelement face 0\nproperty list uchar int vertex_index\nend_header\n" % rows)
	for i in range(rows):
		for j in range(3):
			f.write("%d " % redF[i*3+j])
		f.write("\n")
	f.close() 	
