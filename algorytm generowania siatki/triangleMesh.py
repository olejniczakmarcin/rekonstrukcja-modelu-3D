import open3d as o3d
import numpy as np
import sys
import os

# load .xyz file point cloud
if o3d.io.read_point_cloud("file.xyz", format='xyz').has_points():
    pcd = o3d.io.read_point_cloud("file.xyz", format='xyz')
else:
    print("cloud points empty")
    quit()
# calculate normal vector
pcd.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=0.01, max_nn=30))
# save alpha parameter
if os.path.exists('alpha.txt'):
    os.remove('alpha.txt')
o=open('alpha.txt','a+')

alpha = 0.05
o.writelines(str(alpha))
o.close()
print(f"alpha={alpha:.3f}")
# generate triangle mesh
mesh = o3d.geometry.TriangleMesh.create_from_point_cloud_alpha_shape(pcd, alpha)
mesh.compute_vertex_normals()
# smoothing filter
select_filter='laplasian' # select type filter
number_of_iterationss=2 # select power smoothing

if select_filter=="laplasian":
    mesh_out=mesh.filter_smooth_laplacian(number_of_iterations=number_of_iterationss)
if select_filter=='taubin':
    mesh_out = mesh.filter_smooth_taubin(number_of_iterations=number_of_iterationss)
if select_filter=='simple':
    mesh_out = mesh.filter_smooth_simple(number_of_iterations=number_of_iterationss)
if select_filter=='loop':
    mesh_out = mesh_out.subdivide_loop(number_of_iterations=number_of_iterationss)

# show rezult    
mesh_out.compute_vertex_normals()
o3d.visualization.draw_geometries([mesh_out], mesh_show_back_face=True)
# save to file with .off format
if os.path.exists('siatka.off'):
    os.remove('siatka.off')
ff=open('siatka.off','a+')
vertices = np.asarray(mesh_out.vertices)
trian=np.asarray(mesh_out.triangles)
ff.writelines('OFF\n')
p=str(len(vertices))+' '+str(len(trian))+' '+'0\n'
ff.writelines(p)
# save to file all verticles
for i in range(len(vertices)):
    for j in range(3):
        ff.writelines(str(vertices[i][j]))
        if j<2:
            ff.writelines(' ')
        if j==2:
            ff.writelines('\n')
# save to file all triangles
for i in range(len(trian)):
    ff.writelines('3 ')
    for j in range(3):
        ff.writelines(str(trian[i][j]))
        if j<2:
            ff.writelines(' ')
        if j==2:
            ff.writelines('\n')
ff.close()