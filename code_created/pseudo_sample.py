
from mpl_toolkits import mplot3d

# %matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
import json
import os
# np.set_printoptions(threshold=np.inf, linewidth=np.inf)

n = [2548, 3328, 4212]
r = [3.5, 4, 4.5]
file_path = "/SSD/torch-ngp/data/nerf_synthetic/lego"

def sample_spherical(r, npoints):
    u = np.random.uniform(low=[0, 0],high=[1, 1], size = (npoints,2))
    theta= u.T[0]*np.pi*2
    phi = np.arccos(1-2*u.T[1])

    x = r*np.sin(phi)*np.cos(theta)
    y = r*np.sin(phi)*np.sin(theta)
    z = r*np.cos(phi)
    
    return x, y, z

def extract_coord(pos, r):
    cam_coord_col = []
    for x, y, z in pos:
        a,b,c = x/r, y/r, z/r
        
        d,e,f = -1*a*b,1-b*b,-1*c*b
        l = np.sqrt(d**2+e**2+f**2)
        d,e,f = d/l, e/l, f/l

        g,h,i = np.cross([a,b,c],[d,e,f])     

        cam_coord = [[g,h,i,x]]
        cam_coord.append([d,e,f,y])
        cam_coord.append([a,b,c,z])
        cam_coord.append([0, 0, 0, 1])
        cam_coord_col.append(cam_coord)
    return cam_coord_col

def make_dict(trans_mat):
    f = {
        "camera_angle_x":0.6911112070083618,
        "h": 800,
        "w": 800,
        "frames":[]
        }
    
    for i in range(len(n)):
        for j in range(len(trans_mat[i])):
            frame = {
                        "file_path": f"./pseudo/r_{j}",
                        "rotation": 0,
                        "transform_matrix": trans_mat[i][j]
                    }
            f["frames"].append(frame)
    return f

def main():
    trans_mat = []
    for i in range(len(n)):
        pos = np.array(sample_spherical(r[i], n[i])).T
        
    fig, ax = plt.subplots(1, 1, subplot_kw={'projection':'3d', 'aspect':'equal'})
    ax.scatter3D(pos[0], pos[1], pos[2])
    plt.show()
    #     trans_mat.append(extract_coord(pos, r[i]))
    # dict_file = make_dict(trans_mat)
    # with open(os.path.join(file_path,"transforms_pseudo.json"),'w') as f:
    #     json.dump(dict_file, f)

if __name__ == '__main__':
    main()

# fig, ax = plt.subplots(1, 1, subplot_kw={'projection':'3d', 'aspect':'equal'})
# ax.scatter3D(pos[0], pos[1], pos[2],s=1)
# plt.show()