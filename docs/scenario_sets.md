# Scenario Sets #

Sceanrio Sets are simlilar to the tests within the test_libs. They both describe the order of operations for sequences and scenarios to be exercised. The key difference is that instead of listing out all the combinations of actions you are interested in, like in the test_lib, here in this lib you describe the possible sets of possibilites. These sets would then be used by the test generator to generate all the potential tests, or a single full random test for each scenario set.


all scenario sets will be containted within a test_lib object that has the following structure:

    test_lib[] { set_name, inheritance{}, env_options{}, action_sets[] }
    

## inheritance ##

The inheritance field has the test it extends and also an optional phase_exclusion field. 

Phase exclusion phase field can includue the following entries "run_phase".... by default all generated phases of the test will call the super.phase, doing whatever the extended test has in that location. With this set, it would not be called and overriden.

    Inheritance: {test_name, extends, phase_exclusion[](optional)}

    phase_exclusion [{phase}]

## env_options (optional)

These are all optional fields, if the default base environment configuration needs modified for this test.

### Overriding
Types can be overriden by setting the including the
following objects:

    override_by_type: [ {base_type, overriding_type} ]
    override_by_inst: [ {base_type, overriding_type, path} ]

### Configuration Variables
Component configurations or tests can be set by providing the path and the value

     config_set: [ {path,value} ]

## Generics ##

## Actions ##
Refer to actions.md for available actions.

## Action sets ##
Refer to actions.md for available actions.