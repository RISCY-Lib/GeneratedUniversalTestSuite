# ACTIONS! #

Action items can be included in both Scenario and Test objects. Both of these objects will contain a action list to be traversed through sequentially.

An Action item can be several different types, and depending on the type, will have different item fields. The following section details the available action item types and their fields.

This MD page contains a high-level summary of each action. For more details see the respective page in the ```actions/``` directory.

- [Action Hierarchy](#action-hierarchy)
  - [Higher Level Actions](#higher-level-actions)
  - [Base Actions](#base-actions)
- [Scenario](#scenario)
  - [Scenario Config](#scenario-config)
- [Fork](#fork)
  - [Fork Types](#fork-types)
- [Repeat](#repeat)
- [Sequence](#sequence)
  - [Sequence Config](#sequence-config)
- [Register Transaction](#register-transaction)
- [Delay](#delay)
- [Log](#log)


## Action Hierarchy ##

Some actions can "contain" other actions, these are called "higher level" actions. Others which do not contain other actions are considered "base" actions.

### Higher Level Actions ###
- [Scenario](#scenario)
- [Fork](#fork)
- [Repeat](#repeat)

### Base Actions ###
- [Sequence](#sequence)
- [Register Transaction](#register-transaction)
- [Delay](#delay)
- [Log](#log)

## Scenario ##

See [actions/scenario](actions/scenario.md) for more details.

A Scenario action type includes the information of a specific senario to generate. The scenario library it is a part of must be included, but the configuration option is optional. If no configuration is spefcificed then the Default one will be used.

<!-- TODO: Better define the purpose of scenarios -->

```yaml
type: scenario
scenario_lib: <lib_name>
scenario_name: <scenario_name>
actions:
    - <action1>
    - <action2>
    - ...
    - <actionN>
config: # OPTIONAL
    - <config1>
    - <config2>
    - ...
    - <configN>
```

Type, scenario_lib, scenario_name, and actions are mandatory elements:
- type
    - Must be "scenario"
- scenario_lib
    - The scenario library where the scenario resides
- scenario_name
    - The name of the scenario
- actions
    - A list of actions which compose this scenario

### Scenario Config
- config
    - If no configuration is spefcificed then the Default one will be used. A configuration set will only be considered when in a scenario_set object.

<!-- TODO: define config -->

## Fork ##

See [actions/fork](actions/fork.md) for more details.

A fork action type defines a fork-join pair of a set of actions. It contains a list of actions which each run parallel to each other.

```yaml
type: fork
fork_type: <fork_type> # OPTIONAL
actions:
    - <action1>
    - <action2>
    - ...
    - <actionN>
```

Type and actions are mandatory elements:
- type
    - Must be "fork"
- actions
    - A list of actions which compose this scenario

### Fork Types
The fork type can be one of the following:
- join
- join_any
- join_none

This is an optional field and will default to join if the field is not included.

The actions_prior works exactly as it does for the repeat function.

## Repeat ##

See [actions/repeat](actions/repeat.md) for more details.

A ```repeat``` action causes a set of actions to repeat in order a given number of times.

```yaml
type: repeat
count: <count/count_range>
actions:
    - <action1>
    - <action2>
    - ...
    - <actionN>
```

Type, count and actions are mandatory elements:

- type
  - Must be "repeat"
- Count
  - The number of times to repeat
  - May be a single integer
  - May also be a range in the format ```[[lower:upper]]```
    - A value within ```lower``` and ```upper``` is selected (inclusive)
- Actions
  - A list of actions to loop over



## Sequence ##

See [actions/sequence](actions/sequence.md) for more details.

A Sequence action type includes the information of a specific sequence to generate in the test.

```yaml
type: seq
seq_lib: <lib_name>
seq_name: <seq_name>
config: # OPTIONAL
    - <config1>
    - <config2>
    - ...
    - <configN>
```

Type, seq_lib, and seq_name are all mandatory elements.
- type
    - Must be "seq"
- seq_lib
    - The sequence library where the sequence resides
- seq_name
    - The name of the sequence

### Sequence Config
- config
    - If no configuration is spefcificed then the Default one will be used. A configuration set will only be considered when in a scenario_set object.

<!-- TODO: define config -->

## Register Transaction ##

See [actions/register_transaction](actions/register_transaction.md) for more details.

<!-- TODO: define register transaction action -->

## Delay ##

See [actions/delay](actions/delay.md) for more details.

<!-- TODO: define delay action-->

## Log ##

See [actions/log](actions/log.md) for more details.

<!-- TODO: define log action-->