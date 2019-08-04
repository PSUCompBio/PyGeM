
# coding: utf-8

# In[1]:


#get_ipython().run_line_magic('matplotlib', 'inline')
from pygem import RBFParameters, RBF, StlHandler, VtkHandler
import numpy as np
import matplotlib.pyplot as plt
import os
cwd = os.getcwd()
full_path = os.path.realpath(__file__)
path, filename = os.path.split(full_path)

# In[2]:


params = RBFParameters()
params.read_parameters(filename=path +  '/../tests/test_datasets/parameters_rbf_custom.prm')


# In[2]:


vtk_handler = VtkHandler()
mesh = vtk_handler.parse(path  + '/../tests/test_datasets/Merged.vtk')


# In[4]:


rbf = RBF(params, mesh)
rbf.perform()
new_mesh_points = rbf.modified_mesh_points
vtk_handler.write(new_mesh_points, "brain.vtk")
