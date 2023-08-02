# ACTIONS! #

Action items can be included in both Scenario and Test objects. Both of these objects will contain a action list to be traversed through sequentially.

An Action item can be several different types, and depending on the type, will have different item fields. The following section details the available action item types and their fields.

## Sequence ##

A Sequence action type includes the information of a specific sequence to generate. 

    [ {type:"seq",seq_lib,seq_name,config(optional)},config_set[]]

The sequence library the sequence is a part of, and the sequence_name must be included, but the configuration option is optional. If no configuration is spefcificed then the Default one will be used. A configuration set will only be considered when in a scenario_set object.


## Scenario ##

A Scenario action type includes the information of a specific senario to generate. The scenario library it is a part of must be included, but the configuration option is optional. If no configuration is spefcificed then the Default one will be used.

    [ {type:"scenario",scenario_lib,scenario_name,config(optional), config_set[]}]
## Repeat ##
A set of actions, or the previous action can be repeated through the Repeat action. 

    [ {type:"repeat", repeat_cnt, actions_prior(optional), repeat_range[[min,max]](optional)}]  

The amount of times an action is repeated is determined througn the repeat field.

There is an optional actions_prior that can be set if actions before the disired repeated action should also be included. actions_prior is inclusive of the action before the repeat action, and a value of 0 is not valid. If the actions_prior cnt is not set, then only the action before the repeat action will be repeated. Repeat boundries must be accounted for; If repeat_A repeats actions 0-5, repeat_b cannot include repeat_a and a subset of actions 0-5, it would have to have a <= action list start index.

There is also an optional random repeat range that can be set. if repeat_range is included then
repeat should not be.



Repeat example:

    [
    {
        "type":"seq",
        "seq_lib":"seq_lib_1",
        "seq_name":"seq_name_0"
    },
    {
        "type":"repeat",
        "repeat_cnt":"5"
    }
    {
        "type":"seq",
        "seq_lib":"seq_lib_1",
        "seq_name":"seq_name_1"},
    {
        "type":"seq",
        "seq_lib":"seq_lib_1",
        "seq_name":"seq_name_2"
    },
    {
        "type":"repeat", 
        "repeat_cnt":"7", 
        "actions_prior": "4"
    },
    {
        "type":"seq",
        "seq_lib":"seq_lib_1",
        "seq_name":"seq_name_3"
    },
    {
        "type":"seq",
        "seq_lib":"seq_lib_1",
        "seq_name":"seq_name_4"
    },
    {
        "type":"repeat",
        "actions_prior": "2",
        "repeat_range" : [["1","5"]]
    },
    {
        "type":"repeat",
        "repeat_cnt": "9",
        "actions_prior": "3"
    }
    ]

    Would generate the following in SV:

    repeat(7) begin
        repeat(5) begin
            seq_name_0.start(null);
        end
        seq_name_1.start(null);
        seq_name_2.start(null);
    end
    repeat(9) begin
        repeat ($urandom_range(1,5)) begin
            seq_name_3.start(null);
            seq_name_4.start(null);
        end
    end

## Fork ##
The fork action can be used to run parallel actions.

    [ {type:"fork", fork_type(optional), actions_prior(optional)} ]

The fork type can be one of the following ["join_none", "join_any", "join"]. This is an optional field and will default to join if the field is not included. 

The actions_prior works exactly as it does for the repeat function.

Fork Example:

    [
    {
        "type":"seq",
        "seq_lib":"seq_lib_1",
        "seq_name":"seq_name_0"
    },
    {
        "type":fork
    }
    {
        "type":"seq",
        "seq_lib":"seq_lib_1",
        "seq_name":"seq_name_1"},
    {
        "type":"seq",
        "seq_lib":"seq_lib_1",
        "seq_name":"seq_name_2"
    },
    {
        "type":"fork", 
        "fork_type":"join_none", 
        "actions_prior": "4"
    },
    {
        "type":"seq",
        "seq_lib":"seq_lib_1",
        "seq_name":"seq_name_3"
    },
    {
        "type":"seq",
        "seq_lib":"seq_lib_1",
        "seq_name":"seq_name_4"
    },
    {
        "type":"fork",
        "actions_prior": "2",
        "fork_type": "join_any"
    },
    {
        "type":"fork",
        "actions_prior": "3"
    }
    ]

    Would generate the following in SV:

    fork
        fork
            seq_name_0.start(null);
        join
        seq_name_1.start(null);
        seq_name_2.start(null);
    join_none
    fork
        fork
            seq_name_3.start(null);
            seq_name_4.start(null);
        join_any
    join
 
 ## Log ##

