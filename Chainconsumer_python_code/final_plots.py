#!/usr/bin/env python
# coding: utf-8

# In[28]:


import numpy as np
from numpy.random import normal, multivariate_normal
from chainconsumer import ChainConsumer

# the list of parameters from the header of the output file:
# cosmological_parameters--omega_m    cosmological_parameters--h0 cosmological_parameters--omega_b    cosmological_parameters--n_s    cosmological_parameters--a_s    cosmological_parameters--tau    horndeski_parameters--parameters_smg__2 horndeski_parameters--parameters_smg__3 COSMOLOGICAL_PARAMETERS--SIGMA_8    prior   post

# name these parameters in latex:
params_horndeski = ['$\Omega_m$', '$h_0$', '$\Omega_b$', '$n_s$', '$A_s$', '$\\tau$', '$\\alpha_B$', '$\\alpha_M$', '$\sigma_8$']
params_lcdm = ['$\Omega_m$', '$h_0$', '$\Omega_b$', '$n_s$', '$A_s$', '$\\tau$', '$\sigma_8$']

# write a function for turning the output files into the
# correct format for chainconsumer
def prepare_chain_data(chain_filename, burn_in=5000):

    chain_data = np.loadtxt(chain_filename)
    
    # remove prior and posterior columns, which are not needed
    chain_data = chain_data[:,:-2]

    # make A_s easier to plot
    chain_data[:,4] = chain_data[:,4]*1.e9

    # remove burn-in
    chain_data = chain_data[burn_in:]

    return chain_data

# load the output files
data1 = prepare_chain_data("/Users/abhi/Desktop/SummerProject1/emcee_output/hiclass_dgw.txt")
data2 = prepare_chain_data("/Users/abhi/Desktop/SummerProject1/emcee_output/hiclass_horndeski.txt")
data3 = prepare_chain_data("/Users/abhi/Desktop/SummerProject1/emcee_output/hiclass_lambda_cdm.txt")

# create a plot
c = ChainConsumer()
c.add_chain(data1, parameters=params_horndeski, name="LSS + GW (170817+190521)")
c.add_chain(data2, parameters=params_horndeski, name="LSS with hi_class")
c.add_chain(data3, parameters=params_lcdm, name="Lambda CDM model")
c.configure(colors=['r', 'g', 'b']) 
c.configure(max_ticks=2)

# plot all the parameters
fig1 = c.plotter.plot(filename='./example.png', figsize='column')
fig1.set_size_inches(6 + fig.get_size_inches())
fig1.savefig('All_plots_dgw.png')

# plot only the two alpha parameters
c.configure(max_ticks=5)
fig = c.plotter.plot(parameters=['$\\alpha_B$', '$\\alpha_M$'],
               extents=[[-1.0,2.0],[-1.5,2.0]],
               filename="example_alphas.png",
               figsize="column",)
fig.set_size_inches(4 + fig.get_size_inches())
fig.savefig('Alpha_params.png', )


# In[32]:


import numpy as np
from numpy.random import normal, multivariate_normal
from chainconsumer import ChainConsumer

# the list of parameters from the header of the output file:
# cosmological_parameters--omega_m    cosmological_parameters--h0 cosmological_parameters--omega_b    cosmological_parameters--n_s    cosmological_parameters--a_s    cosmological_parameters--tau    horndeski_parameters--parameters_smg__2 horndeski_parameters--parameters_smg__3 COSMOLOGICAL_PARAMETERS--SIGMA_8    prior   post

# name these parameters in latex:
params_horndeski = ['$\Omega_m$', '$h_0$', '$\Omega_b$', '$n_s$', '$A_s$', '$\\tau$', '$\\alpha_B$', '$\\alpha_M$', '$\sigma_8$']
params_lcdm = ['$\Omega_m$', '$h_0$', '$\Omega_b$', '$n_s$', '$A_s$', '$\\tau$', '$\sigma_8$']

# write a function for turning the output files into the
# correct format for chainconsumer
def prepare_chain_data(chain_filename, burn_in=5000):

    chain_data = np.loadtxt(chain_filename)
    
    # remove prior and posterior columns, which are not needed
    chain_data = chain_data[:,:-2]

    # make A_s easier to plot
    chain_data[:,4] = chain_data[:,4]*1.e9

    # remove burn-in
    chain_data = chain_data[burn_in:]

    return chain_data

# load the output files
#data1 = prepare_chain_data("/Users/abhi/Desktop/SummerProject1/emcee_output/hiclass_dgw.txt")
data2 = prepare_chain_data("/Users/abhi/Desktop/SummerProject1/emcee_output/hiclass_horndeski.txt")
#data3 = prepare_chain_data("/Users/abhi/Desktop/SummerProject1/emcee_output/hiclass_lambda_cdm.txt")

# create a plot
c = ChainConsumer()
#c.add_chain(data1, parameters=params_horndeski, name="hiclass_dgw")
c.add_chain(data2, parameters=params_horndeski, name="LSS with hi_class")
#c.add_chain(data3, parameters=params_lcdm, name="hiclass_lambda_cdm")
c.configure(colors=['b']) 
c.configure(max_ticks=2)

# plot all the parameters
fig1 = c.plotter.plot(filename='./example.png', figsize='column')
fig1.set_size_inches(6 + fig.get_size_inches())
fig1.savefig('All_plots_dgw1.png')

# plot only the two alpha parameters
c.configure(max_ticks=5)
fig = c.plotter.plot(parameters=['$\\alpha_B$', '$\\alpha_M$'],
               extents=[[-1.0,2.0],[-1.5,2.0]],
               filename="example_alphas.png",
               figsize="column",)
fig.set_size_inches(4 + fig.get_size_inches())
fig.savefig('Alpha_params1.png', )


# In[30]:


import numpy as np
from numpy.random import normal, multivariate_normal
from chainconsumer import ChainConsumer

# the list of parameters from the header of the output file:
# cosmological_parameters--omega_m    cosmological_parameters--h0 cosmological_parameters--omega_b    cosmological_parameters--n_s    cosmological_parameters--a_s    cosmological_parameters--tau    horndeski_parameters--parameters_smg__2 horndeski_parameters--parameters_smg__3 COSMOLOGICAL_PARAMETERS--SIGMA_8    prior   post

# name these parameters in latex:
params_horndeski = ['$\Omega_m$', '$h_0$', '$\Omega_b$', '$n_s$', '$A_s$', '$\\tau$', '$\\alpha_B$', '$\\alpha_M$', '$\sigma_8$']
params_lcdm = ['$\Omega_m$', '$h_0$', '$\Omega_b$', '$n_s$', '$A_s$', '$\\tau$', '$\sigma_8$']

# write a function for turning the output files into the
# correct format for chainconsumer
def prepare_chain_data(chain_filename, burn_in=5000):

    chain_data = np.loadtxt(chain_filename)
    
    # remove prior and posterior columns, which are not needed
    chain_data = chain_data[:,:-2]

    # make A_s easier to plot
    chain_data[:,4] = chain_data[:,4]*1.e9

    # remove burn-in
    chain_data = chain_data[burn_in:]

    return chain_data

# load the output files
#data1 = prepare_chain_data("/Users/abhi/Desktop/SummerProject1/emcee_output/hiclass_dgw.txt")
#data2 = prepare_chain_data("/Users/abhi/Desktop/SummerProject1/emcee_output/hiclass_horndeski.txt")
data3 = prepare_chain_data("/Users/abhi/Desktop/SummerProject1/emcee_output/hiclass_lambda_cdm.txt")
# create a plot
c = ChainConsumer()
#c.add_chain(data1, parameters=params_horndeski, name="hiclass_dgw")
#c.add_chain(data2, parameters=params_horndeski, name="hiclass_horndeski")
c.add_chain(data3, parameters=params_lcdm, name="hiclass_lambda_cdm")
c.configure(colors=['r', 'g', 'b']) 
c.configure(max_ticks=2)

# plot all the parameters
fig1 = c.plotter.plot(filename='./example.png', figsize='column')
fig1.set_size_inches(6 + fig.get_size_inches())
fig1.savefig('All_plots_dgw2.png')

# plot only the two alpha parameters
#c.configure(max_ticks=5)
#fig = c.plotter.plot(parameters=['$\\alpha_B$', '$\\alpha_M$'],
               #extents=[[-1.0,2.0],[-1.5,2.0]],
               #filename="example_alphas.png",
               #figsize="column",)
#fig.set_size_inches(4 + fig.get_size_inches())


# In[31]:


import numpy as np
from numpy.random import normal, multivariate_normal
from chainconsumer import ChainConsumer

# the list of parameters from the header of the output file:
# cosmological_parameters--omega_m    cosmological_parameters--h0 cosmological_parameters--omega_b    cosmological_parameters--n_s    cosmological_parameters--a_s    cosmological_parameters--tau    horndeski_parameters--parameters_smg__2 horndeski_parameters--parameters_smg__3 COSMOLOGICAL_PARAMETERS--SIGMA_8    prior   post

# name these parameters in latex:
params_horndeski = ['$\Omega_m$', '$h_0$', '$\Omega_b$', '$n_s$', '$A_s$', '$\\tau$', '$\\alpha_B$', '$\\alpha_M$', '$\sigma_8$']
params_lcdm = ['$\Omega_m$', '$h_0$', '$\Omega_b$', '$n_s$', '$A_s$', '$\\tau$', '$\sigma_8$']

# write a function for turning the output files into the
# correct format for chainconsumer
def prepare_chain_data(chain_filename, burn_in=5000):

    chain_data = np.loadtxt(chain_filename)
    
    # remove prior and posterior columns, which are not needed
    chain_data = chain_data[:,:-2]

    # make A_s easier to plot
    chain_data[:,4] = chain_data[:,4]*1.e9

    # remove burn-in
    chain_data = chain_data[burn_in:]

    return chain_data

# load the output files
data1 = prepare_chain_data('/Users/abhi/Desktop/SummerProject1/gw170817/Output/alpha_m_1/distances/d_l_gw_on_d_l_em.txt')
data2 = prepare_chain_data("/Users/abhi/Desktop/SummerProject1/gw170817/Output/alpha_m_2/distances/d_l_gw_on_d_l_em.txt")
data3 = prepare_chain_data("'/Users/abhi/Desktop/SummerProject1/gw170817/Output/alpha_m_3/distances/d_l_gw_on_d_l_em.txt")

# create a plot
c = ChainConsumer()
c.add_chain(data1, parameters=params_horndeski, name="hiclass_dgw")
c.add_chain(data2, parameters=params_horndeski, name="hiclass_horndeski")
c.add_chain(data3, parameters=params_lcdm, name="hiclass_lambda_cdm")
c.configure(colors=['r', 'g', 'b']) 
c.configure(max_ticks=2)

# plot all the parameters
fig1 = c.plotter.plot(filename='./example.png', figsize='column')
fig1.set_size_inches(6 + fig.get_size_inches())
#fig1.savefig('All_plots_dgw.png')

# plot only the two alpha parameters
c.configure(max_ticks=5)
fig = c.plotter.plot(parameters=['$\\alpha_B$', '$\\alpha_M$'],
               extents=[[-1.0,2.0],[-1.5,2.0]],
               filename="example_alphas.png",
               figsize="column",)
fig.set_size_inches(4 + fig.get_size_inches())
#fig.savefig('Alpha_param


# In[ ]:




