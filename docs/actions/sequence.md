# Sequences #

Sequences are the atomic operations used in GUTS.
All sequences will be containted within a seq_lib object.

- [Schema](#schema)
- [Type Element](#type-element)
- [Name Element](#type-element)
- [Config Element](#config-element)
- [Config-Param Element](#config-param-element)
- [Config-Var Element](#config-var-element)
- [Example](#example)

## Schema

```yaml
type: sequence
name: <seuence name>
config: <config>
    - <config1>
    - <config2>
    ...
```
## Type Element
This is the action type tag.
For a ```sequence``` it must be the string literal ```"sequence"```.

## Name Element
This is the aname of the sequence.

## Config Element
The *optional* config element (using tag ```config```) is an array
of params and seq variables that will be used to create the sequence.

```yaml
name:
param: <param> # OPTIONAL
    - <param1>
    - <param2>
    ...
var: <var> # OPTIONAL
    - <var1>
    - <var2>
    ...
```

## Config-Name Element
Name of the configuration that can be referenced in other parts of the generator.

## Config-Param Element
The *optional* param element (using tag ```param```) is an array
of name-value pairs that are used in the creation of the sequence.
```yaml
name:  "param_name"
value: "param_value"
...
```

## Config-Var Element
The *optional* var element (using tag ```var```) is an array
of sequence variables that are assigned after sequence creation.
```yaml
name:  "var_name"
value: "var_value" # OPTIONAL
range: "min,max" # OPTIONAL
list: <list> # OPTIONAL
    - <value1>
    - <value2>
    ...
```

The name of the variable is required and either value, range, or list must be configured. Value is the assignment element. Range is intended for integer types; to specify boundries of the int - a random value from within this range will be assigned to the parameter when creating the sequence. The list allows for integer and non-integer types to be selected randomly from the list.

## Example

```json
{
    "type": "sequence",
    "name": "sequence_1",
    "config": [
        {
            "name": "full_boundry",
            "param": [
                {
                    "name" : "BUS_WIDTH",
                    "value": "32"
                }],
            "var": [
                {
                    "name" : "var1",
                    "range": [{"1","10"}]
                },
                {
                    "name" : "var2",
                    "value": "16"
                },
                {
                    "name" : "var3",
                    "list": [{"1","10","12", "17"}]
                },
                ]
        }
    ]
}
```
Would generate the following API sv task:

```verilog

task start_sequence_1_full_boundry(
    input var1_min = 1;
    input var1_max = 10;
    input var3_list[] = {1,10,12,17});

    //Variables
    sequence_1 sequence_1_h;
    integer var1_rand_range;
    integer var3_rand_list_item;
    var1_rand_range = $urandom_range(var1_min, var1_max);
    std::randomize(var3_rand_list_item) with {var3_rand_list_item inside {var3_list};};
    //Create Seq
    sequence_1_h = sequence_1#(.BUS_WIDTH(32))::type_id::create("sequence_1_h");
    //Assign Variables
    sequence_1_h.var1 = var1_rand_range;
    sequence_1_h.var2 = 16;
    sequence_1_h.var3 = var3_rand_list_item;
    //Start Seq
    uvm_report_info("start_sequence_1_full_boundry", $sformatf("START of SEQ"), UVM_LOW);
    phase.raise_objection(this, "Objection raised by start_sequence_1_full_boundry");
    sequence_1_h.start(m_env.m_virtual_sequencer);
    uvm_report_info("start_sequence_1_full_boundry", $sformatf("END of SEQ"), UVM_LOW);
    phase.drop_objection(this, "Objection dropped by start_sequence_1_full_boundry");

endtask
```