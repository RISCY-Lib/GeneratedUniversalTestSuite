# Test Generator #
Tests can be generated with the following cmd

    GUTS.py [OPTIONS] --tests [TEST_LIB] --sets [SCENARIO_SETS_LIB] --seqs [SEQUENCE_LIB] --scenarios [SCENARIOS_LIB] 

A test_lib.json or scenario_sets_lib.json file, a seq_lib.json, and a scenarios_lib.json is required to generate tests. The optional arguments are listed below.

## Arguments ##

    --test_gen_loc [PATH]
Tests will be generated and placed in ./generated_tests if the --test_gen_loc is not used.

    --reg_model reg_model
If a reg_model is passed, the test scenarios and sequences will be scraped to come up with an estimated pre-test register coverage, whcih may differ from what actually occurs due to randomness. Only the included reg_util.svh operations will be scraped. ##TODO include optional scrape args?

    --only_scenario_set_tests
Only the scenario set tests will be generated.

    --only_scenario_set_random_tests
Only the full random scenario set tests will be generated

    --exclude_test {test_1,test_2}
An exclusion list of test names can be included to exclude thier generation

    --only_test_gen {test_1}
An inclusion test list, only these ones will be generated

    --post_test_log
    --post_test_ucdb

For post test report to be generate, the --post_test_log must be included
If coverage statistics are to be populated in the report, the UCDB must also be inlcuded.

    --env_file env.svh
The testbench enviroment can be passed to generate a visual diagram of all the connected components.


## Output Artifacts ##
Below the outputted artifacts are listed.

    ./GUTS
        ./tests_gen/
            test_1.svh
            test_2.svh
        ./scenario_tests_gen/
            test_1.svh
        ./test_descriptions/ 
            test_1_summary.html
        ./pre_test_coverage/
            test_cov_summary.html
            test_1_cov.html
            test_2_cov.html
        ./post_test_reports/
            test_cov_summary.html
            test_1_report.html
            test_2_report.html


### generated_tests ###
This directory includes all of the generated tests, generated from the included passed test_lib.
### scenario_sets_tests ###
This directory includes all of the generated tests possible from the coverage scenarios within the passed scenario_sets_lib.
### test_descriptions ###
This directory includes all of the test_descriptions. The description includes a diagram of the potential ordering of events (scenarios and tests being run) and a step by step list of what is being done in the test. It also lists all enviroment configurations or overrides. If the env file is passeed then it will also include a diagram of the conected UVM components.
### Pre-test coverage ###
This directory will contain the register coverage for each test and a merged reg coverage if the reg_model argument is passed. It will also include the sequence and scenario statitics; how many are used in the test, what configurations of each are used.
### Post-test coverage ###
This directory will contain a report for each test that was run. The report will include the register coverage for each test and a merged reg coverage if the UCDB argument is passed. It will include a diagram showing the sequence of actions that were taken, and highlight in the diagram where an error, if any, occured. The step by step actions that were taken will also be listed. The logs will be organized by action; each action will have its own log section. If the action is a scenario, it will have additional secitons within it; one for wach sequence.