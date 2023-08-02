# Sequences #

Sequences are the atomic operations used in GUTS, all individual reg read/write/force operations should be contained within a sequence.

All tests will be containted within a seq_lib object that has the following structure:

    seq_lib[] { seq_name, configurations[](optional) }

## configurations

If a sequence contains paramters, combinations of their values or full randomization of them can be assigned a string value, that can be referenced by higher level scenarios and tests 

    configurations: [{config_name, params[]}]
    params: [{param_name, param_value, param_range[["min","max"]]}, param_rand_list{}]

For each configuration item, a config_name must be given. The param object must have the param_name filled in, and must contain either a param_value, param_range, or param_rand_list. The param_range is an integer max min list, that generates a $urandom_range(min,max) in the sequence calls. The random list field places a random list item in the sequence call.

