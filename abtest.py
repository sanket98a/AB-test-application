from functools import reduce
import pandas as pd
import numpy as np

from scipy.stats import beta,invgamma,norm

import matplotlib.pyplot as plt
import seaborn as sns
# set prior_alpha & prior_beta to 1
prior_alpha=1
prior_beta=1

def BayesianApproach(control_retained,test_retained,total_control,total_treatment):
    """
    
    """
    print("Stats of Data Loading...")
    
    # find the converted total for Non control group
    control_non_retained=total_control-control_retained

    # find the converted total for Non treatment group
    test_non_retained=total_treatment-test_retained
    
    # Update Prior parameters with experiment conversion rates
#     global posterior_control
    posterior_control = beta(prior_alpha + control_retained, prior_beta + control_non_retained)
#     global posterior_treatment
    posterior_treatment = beta(prior_alpha + test_retained, prior_beta + test_non_retained)
    
    # Sample from Posteriors
    control_samples = posterior_control.rvs(1000)
    treatment_samples = posterior_treatment.rvs(1000)
    
    # samples=list(zip(treatment_samples,control_samples))
    
    # diff_list1 = map(lambda sample: np.max([sample[0]-sample[1], 0]), samples)
    # sum_diff1 = reduce(lambda x,y:x+y, diff_list1)
    # EL_CONTROL = (sum_diff1/1000) * 100
    
    # diff_list2 = map(lambda sample: np.max([sample[1]-sample[0], 0]), samples)
    # sum_diff2 = reduce(lambda x,y:x+y, diff_list2)
    # EL_TREAT = (sum_diff2/1000) * 100
    # print(EL_CONTROL)
    # print(EL_TREAT)
    
    # probability of treatment > control
    probability = round(np.mean(treatment_samples > control_samples),2)
   
    if probability > 0.95:
        ans=f"Treatment is the winner!\n(Based on 95% significance level) >> {probability}"
        color=['g','r']
    elif 1-probability>0.95:
        ans=f"Control is the winner!\n(Based on 95% significance level) >> {1-probability}"
        color=['r','g']
    else:
        ans="No winner has been declared yet.\n(Based on 95% significance level)"
        color=['b','b']

#     probability_list.append(probability*100)
    # find out lift percentage then check the probability of 2%
    lift_percentage = (treatment_samples - control_samples) / control_samples
    lift=f"Probability that we are seeing a 2% lift: {np.mean((100 * lift_percentage) > 2) * 100}%"
    return probability,ans,lift,treatment_samples,control_samples,color
    
