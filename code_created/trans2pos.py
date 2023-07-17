
import json
import os

from mpl_toolkits import mplot3d

# %matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
import math

dir_path = "./lego"
file_name = "transforms_train.json"
with open(os.path.join(dir_path,file_name), 'r') as f:
    json_data = json.load(f)

pos = []
dist = []

for frame in json_data["frames"]:
    p = []
    for i in range(3):
        p.append(frame["transform_matrix"][i][3])
    dist.append(math.sqrt(p[0]**2+p[1]**2+p[2]**2))
    pos.append(p)
# print(dist)
# plt.hist(dist, bins=30)

pos = np.array(pos).T

pos[0][0], pos[0][1], pos[0][2]

# ax = plt.axes(projection='3d')

theta = np.linspace(0, np.pi, 20)
phi = np.linspace(-np.pi/2, np.pi/2, 40)
x = np.outer(np.sin(phi), np.cos(theta))*4
y = np.outer(np.sin(phi), np.sin(theta))*4
z = np.outer(np.cos(phi), np.ones_like(theta))*4

fig, ax = plt.subplots(1, 1, subplot_kw={'projection':'3d', 'aspect':'equal'})
ax.plot_wireframe(x, y, z, color='gray', rstride=1, cstride=1)
ax.scatter3D(pos[0], pos[1], pos[2])
plt.show()

