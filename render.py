import os
import pyvista as pv
import numpy as np
import vtk

bunny = open("bunny.m").readlines()
vertex, face = [], []
for Line in bunny:
    Line = Line.replace("(", " ")
    Line = Line.replace(")", " ")
    string = Line.strip("\n").split()
    if string[0] == 'Vertex':
        pos = [string[2], string[3], string[4], string[6], string[7], string[8]]
        vertex.append([float(val) for val in pos])
    elif string[0] == 'Face':
        pos = [4, string[2], string[3], string[4]]
        face.append([int(val)-1 for val in pos])
    else:
        print('error')

vertex = np.array(vertex)
cells = []
for i in range(len(face)):
    cells.append(face[i])
cells = np.array(cells).ravel()
cell_types = np.empty(len(face), dtype=np.uint8)
cell_types[:] = vtk.VTK_TRIANGLE
mesh = pv.UnstructuredGrid(cells, cell_types, vertex[:, :3])
center_point = np.array(mesh.center)
mesh.save('./bunny.vtk')
