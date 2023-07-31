# **Tests**

All tests will be containted within a test_lib object that has the following structure:

    test_lib[] { test_name, inheritance{}, env_options{}, Actions[] }
    

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

## Example Test ##
test_1 entry of test_lib_ex.json would generate the follwoing sv:

    Generated Code:
    class test_1 extends base_test;
    
        `uvm_component_utils( test_1 );

        function new( string name = "", uvm_component parent = null );
            super.new( name, parent );
        endfunction

        virtual function void end_of_elaboration_phase(uvm_phase phase);
            super.end_of_elaboration_phase(phase);

             phase.raise_objection(this, "Objection raised by test_1");

            //Type Overrides
            type_a::type_id::set_type_override(type_b::get_type());
            type_b::type_id::set_type_override(type_c::get_type());

            //Instance Overrides
            type_a::type_id::set_inst_override(type_b::get_type(),"inst1.*", this);
            type_b::type_id::set_inst_override(type_c::get_type(),"inst2.*", this);

            //Configurations
            m_env_cfg.clk_rst_agent_cfg.rst_time = 10us;
            m_env_cfg.clk_rst_agent_cfg.clk_period = 10ns;

            phase.drop_objection(this, "Objection dropped by test_1");
        endfunction

        virtual function void run_phase(uvm_phase phase);
            super.run_phase(phase);
            phase.raise_objection(this, "Objection raised by test_1");

            repeat(7) begin
                seq_name_0.start(null);
                scenario_name_0.start(null);
            end

            phase.drop_objection(this, "Objection dropped by test_1");
        endfunction

    endclass

schema file:
[]()