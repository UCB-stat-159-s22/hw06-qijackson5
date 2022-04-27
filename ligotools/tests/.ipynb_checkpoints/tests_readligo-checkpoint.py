from ligotools import readligo as rl

# test if the loaddata function works properly on H1
def test_loaddata_forH1():
    fn_H1 = "data/H-H1_LOSC_4_V2-1126259446-32.hdf5"
    strain_H1, time_H1, chan_dict_H1 = rl.loaddata(fn_H1, 'H1')
    assert (strain_H1.any())
    assert (time_H1.any())
    assert (chan_dict_H1 is not None)
    
# test if the loaddata function works properly on L1
def test_loaddata_forL1():
    fn_L1 = "data/L-L1_LOSC_4_V2-1126259446-32.hdf5"
    strain_L1, time_L1, chan_dict_L1 = rl.loaddata(fn_L1, 'L1')
    assert (strain_L1.any())
    assert (time_L1.any())
    assert (chan_dict_H1 is not None)

    
# test if the dq_channel_to_seglist function works on h1 checking the length of the segment list
def test_dq_channel_to_seglist_CBC():
    fn_L1 = "data/L-L1_LOSC_4_V2-1126259446-32.hdf5"
    strain, time, chan_dict = rl.loaddata(fn_L1, 'H1')
    DQflag = 'CBC_CAT3'
    segment_list = rl.dq_channel_to_seglist(chan_dict[DQflag])
    actual_length = 1
    assert(len(segment_list) == actual_length)

# test if the dq_channel_to_seglist function outputs the right segment list that we want for no CBC hardware injections:
def test_dq_channel_to_seglist_no_CBC():
    fn_L1 = "data/L-L1_LOSC_4_V2-1126259446-32.hdf5"
    strain, time, chan_dict = rl.loaddata(fn_L1, 'H1')
    DQflag = 'NO_CBC_HW_INJ'
    segment_list = rl.dq_channel_to_seglist(chan_dict[DQflag])
    actual_list = [slice(0, 131072, None)]
    assert(segment_list == actual_list)

    
    