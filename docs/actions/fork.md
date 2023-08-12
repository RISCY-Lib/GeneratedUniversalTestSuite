# Fork

A fork action type defines a fork-join pair of a set of actions.
It contains a list of actions which each run parallel to each other.

- [Schema](#schema)
- [Type Element](#type-element)
- [Fork-Type Element](#fork-type-element)
- [Actions Element](#actions-element)
- [Example](#example)

## Schema

```yaml
type: fork
fork_type: <fork_type> # OPTIONAL
actions:
    - <action1>
    - <action2>
    - ...
    - <actionN>
```

## Type Element
This is the action type tag.
For a ```fork``` it must be the string literal ```"fork"```.

## Fork-Type Element
The *optional* fork-type element (using tag ```fork_type```) of the ```fork``` action is the method of determining the type of fork.
It must be one of the following string literals:
- ```"join"``` **(Default)**
- ```"join_any"```
- ```"fork_none"```

These correspond to their respective SystemVerilog implementations.

## Actions Element
The actions element of the ```fork``` action is a list of actions which are forked inside the fork.

This list can be any valid action including other forks.

## Example
```json
{
    "type": "fork",
    "fork_type": "join_none",
    "actions": [
        {
            "type": "fork",
            "fork_type": "join",
            "actions": [
                {
                    "type": "seq",
                    "seq_lib": "seq_lib",
                    "seq_name": "seq_name_0"
                },
                {
                    "type": "seq",
                    "seq_lib": "seq_lib",
                    "seq_name": "seq_name_1"
                }
            ]
        },
        {
            "type": "seq",
            "seq_lib": "seq_lib",
            "seq_name": "seq_name_2"
        }
    ]
},
{
    "type": "fork",
    "fork_type": "join_any",
    "actions": [
        {
            "type": "seq",
            "seq_lib": "seq_lib",
            "seq_name": "seq_name_3"
        },
        {
            "type": "seq",
            "seq_lib": "seq_lib",
            "seq_name": "seq_name_4"
        }
    ]
}
```

Would represent the following in SV:

```verilog
fork
    fork
        seq_name_0.start(null);
        seq_name_1.start(null);
    join
    seq_name_2.start(null);
join_none

fork
    seq_name_3.start(null);
    seq_name_4.start(null);
join_any
```