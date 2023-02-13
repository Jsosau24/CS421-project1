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
    corrections = algo.attach(np_array, line_ys)
    percentage, match_list = correction.correction_quality(aoi, robot_data.copy(), corrections)

    return percentage, corrections, match_list

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
    corrections = algo.chain(np_array, line_ys)
    percentage, match_list = correction.correction_quality(aoi, robot_data.copy(), corrections)

    return percentage, corrections, match_list

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
    corrections = algo.regress(np_array, line_ys)
    percentage, match_list = correction.correction_quality(aoi, robot_data.copy(), corrections)

    return percentage, corrections, match_list

def warp_correction(data, word_centers, aoi, robot_data):
    '''
    corrects the data with the noise using the warp algorithm

    Parameters
    ------------------------------
    data: data with the error
    word_centers: xy coordinates for the word centers
    aoi: areas of interest
    robot_data: gets the data from the robot
    '''
    np_array = np.array(data.copy(), dtype=int)
    durations = np.delete(np_array, 0, 1)
    durations = np.delete(durations, 0, 1)
    np_array = np.delete(np_array, 2, 1)
        
    corrections = algo.warp(np_array, word_centers)
    percentage, match_list = correction.correction_quality(aoi, robot_data.copy(), corrections)
    
    return percentage, corrections, match_list

def cluster_correction(data, line_ys, aoi, robot_data):
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
    corrections = algo.cluster(np_array, line_ys)
    percentage, match_list = correction.correction_quality(aoi, robot_data.copy(), corrections)

    return percentage, corrections, match_list

def compare_correction(data, line_ys, word_centers, aoi, robot_data):
    '''
    corrects the data with the noise using the compare algorithm

    Parameters
    ------------------------------
    data: data with the error
    line_ys: y = y coordinates for each line
    word_centers: xy coordinates for the word centers
    aoi: areas of interest
    robot_data: gets the data from the robot
    '''

    np_array = np.array(data.copy())
    corrections = algo.compare(np_array, line_ys, word_centers)
    percentage, match_list = correction.correction_quality(aoi, robot_data.copy(), corrections)
    
    return percentage, corrections, match_list

def merge_correction(data, line_ys, aoi, robot_data):
    '''
    corrects the data with the noise using the merge algorithm

    Parameters
    ------------------------------
    data: data with the error
    line_ys: y = y coordinates for each line
    aoi: areas of interest
    robot_data: gets the data from the robot
    '''

    np_array = np.array(data.copy())
    corrections = algo.merge(np_array, line_ys)
    percentage, match_list = correction.correction_quality(aoi, robot_data.copy(), corrections)

    return percentage, corrections, match_list

def segment_correction(data, line_ys, aoi, robot_data):
    '''
    corrects the data with the noise using the segment algorithm

    Parameters
    ------------------------------
    data: data with the error
    line_ys: y = y coordinates for each line
    aoi: areas of interest
    robot_data: gets the data from the robot
    '''

    np_array = np.array(data.copy())
    corrections = algo.segment(np_array, line_ys)
    percentage, match_list = correction.correction_quality(aoi, robot_data.copy(), corrections)

    return percentage, corrections, match_list

def split_correction(data, line_ys, aoi, robot_data):
    '''
    corrects the data with the noise using the split algorithm

    Parameters
    ------------------------------
    data: data with the error
    line_ys: y = y coordinates for each line
    aoi: areas of interest
    robot_data: gets the data from the robot
    '''

    np_array = np.array(data.copy())
    corrections = algo.split(np_array, line_ys)
    percentage, match_list = correction.correction_quality(aoi, robot_data.copy(), corrections)

    return percentage, corrections, match_list

def stretch_correction(data, line_ys, aoi, robot_data):
    '''
    corrects the data with the noise using the stretch algorithm

    Parameters
    ------------------------------
    data: data with the error
    line_ys: y = y coordinates for each line
    aoi: areas of interest
    robot_data: gets the data from the robot
    '''

    np_array = np.array(data.copy())
    corrections = algo.stretch(np_array, line_ys)
    percentage, match_list = correction.correction_quality(aoi, robot_data.copy(), corrections)

    return percentage, corrections, match_list

def get_x_fixations_per_line (fixations, line_ys):
    '''returns a 2d array with the fixations in x per line'''

    x_fix = []

    for i in range(len(line_ys)):
        x_fix.append([])

    for fix in fixations:
        
        x, y= fix[0], fix[1]

        for i in range(len(line_ys)):
            if ((line_ys[i]-25) <= y <= (line_ys[i]+25) ):
                x_fix[i].append(y)
                break

    return x_fix

        











