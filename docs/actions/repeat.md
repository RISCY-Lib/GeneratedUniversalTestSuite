# Repeat

A ```repeat``` action causes a set of actions to repeat in order a given number of times.

## Schema

```yaml
type: repeat
count: <count/count_range>
actions:
    - <action1>
    - <action2>
    - ...
    - <actionN>
```

## Type Element
<!-- TODO -->

## Count Element
<!-- TODO -->

## Actions Element
<!-- TODO -->

## Example

```json
{
    "type": "repeat",
    "count": 7,
    "actions": [
        {
            "type": "repeat",
            "count": 5,
            "actions": [
                {
                    "type": "seq",
                    "seq_lib": "seq_lib",
                    "seq_name": "seq_name_0"
                }
            ]
        },
        {
            "type": "seq",
            "seq_lib": "seq_lib",
            "seq_name": "seq_name_1"
        },
        {
            "type": "seq",
            "seq_lib": "seq_lib",
            "seq_name": "seq_name_2"
        }
    ]
},
{
    "type": "repeat",
    "count": 9,
    "actions": [
        {
            "type": "repeat",
            "count": [[1, 5]],
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
    ]
}
```

Would represent the following in SV:

```verilog
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
```