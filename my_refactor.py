'''
Jonathan Sosa
my_refactor.py
Feb 2023
'''

#imports
import emip_toolkit as EMTK
import correction
import numpy as np
import drift_algorithms as algo
from tqdm import tqdm

#functions
def attach_correction(data, line_ys, aoi, robot_data):
    '''
    corrects the data with the noise using the attach algorithm

    Parameters
    ------------------------------
    data: data with the error
    line_ys: y = y coordinates for each line
    aoi: areas of interest
    robot_index: gets the index of the robot we are testing the data on
    '''

    np_array = np.array(data.copy())
    attach_correction = algo.attach(np_array, line_ys)
    percentage, match_list = correction.correction_quality(aoi, robot_data.copy(), attach_correction)

    return percentage

def chain_correction(data, line_ys, aoi, robot_data):
    '''
    corrects the data with the noise using the chain algorithm

    Parameters
    ------------------------------
    data: data with the error
    line_ys: y = y coordinates for each line
    aoi: areas of interest
    robot_data: gets the data from the robot
    '''

    np_array = np.array(data.copy())
    chain_correction = algo.chain(np_array, line_ys)
    percentage, match_list = correction.correction_quality(aoi, robot_data.copy(), chain_correction)

    return percentage

def regress_correction(data, line_ys, aoi, robot_data):
    '''
    corrects the data with the noise using the regress algorithm

    Parameters
    ------------------------------
    data: data with the error
    line_ys: y = y coordinates for each line
    aoi: areas of interest
    robot_data: gets the data from the robot
    '''

    np_array = np.array(data.copy())
    regress_correction = algo.regress(np_array, line_ys)
    percentage, match_list = correction.correction_quality(aoi, robot_data.copy(), regress_correction)

    return percentage

def warp_correction(data, word_centers, aoi, robot_data):
    '''
    corrects the data with the noise using the warp algorithm

    Parameters
    ------------------------------
    data: data with the error
    line_ys: y = y coordinates for each line
    aoi: areas of interest
    robot_data: gets the data from the robot
    '''
    np_array = np.array(data.copy(), dtype=int)
    durations = np.delete(np_array, 0, 1)
    durations = np.delete(durations, 0, 1)
    np_array = np.delete(np_array, 2, 1)
        
    warp_correction = algo.warp(np_array, word_centers)
    percentage, match_list = correction.correction_quality(aoi, robot_data.copy(), warp_correction)
    
    return percentage, warp_correction, match_list









