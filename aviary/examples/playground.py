import aviary.api as av


throttle_max = 1.0
throttle_climb = 0.956
throttle_cruise = 0.930
throttle_idle = 0.0


subsystem_options = {'core_aerodynamics':
                     {'method': 'low_speed',
                      'ground_altitude': 0.,  # units='ft'
                      'angles_of_attack': [
                          0.0, 1.0, 2.0, 3.0, 4.0, 5.0,
                          6.0, 7.0, 8.0, 9.0, 10.0, 11.0,
                          12.0, 13.0, 14.0, 15.0],  # units='deg'
                      'lift_coefficients': [
                          0.5178, 0.6, 0.75, 0.85, 0.95, 1.05,
                          1.15, 1.25, 1.35, 1.5, 1.6, 1.7,
                          1.8, 1.85, 1.9, 1.95],
                      'drag_coefficients': [
                          0.0674, 0.065, 0.065, 0.07, 0.072, 0.076,
                          0.084, 0.09, 0.10, 0.11, 0.12, 0.13,
                          0.15, 0.16, 0.18, 0.20],
                      'lift_coefficient_factor': 1.,
                      'drag_coefficient_factor': 1.}}

phase_info = {
    "pre_mission": {"include_takeoff": False, "optimize_mass": False},
    'AB': {
        'user_options': {
            'num_segments': 5,
            'order': 3,
            'fix_initial': True,
            'ground_roll': True,
            'duration_ref': (100., 'kn'),
            'duration_bounds': ((1., 500.), 'kn'),
            'constraints': {
                # 'TAS': {
                #     'equals': 120.,  # V_rot
                #     'loc': 'final',
                #     'units': 'kn',
                #     'type': 'boundary',
                # },
                # 'distance': {
                #     'equals': 8000.,
                #     'loc': 'final',
                #     'units': 'ft',
                #     'type': 'boundary',
                # },
                # 'time': {
                #     'upper': 80.,
                #     'loc': 'final',
                #     'units': 's',
                #     'type': 'boundary',
                # },
            },
        },
        'subsystem_options': subsystem_options,
        'initial_guesses': {
            'distance': [(0., 2.e3), 'ft'],
            'time': [(0., 20.), 's'],
            'velocity': [(1., 120.), 'kn'],
            'mass': [(175.e3, 175.e3-100.), 'lbm'],
            # 'altitude': [(0., 0.), 'ft'],
        },
    },
    'rotate': {
        'user_options': {
            'num_segments': 5,
            'order': 3,
            'fix_initial': False,
            'throttle_setting': throttle_max,
            'input_speed_type': av.SpeedType.TAS,
            'ground_roll': True,
            'clean': False,
            'initial_ref': (1.e3, 'ft'),
            'initial_bounds': ((1., 16.e3), 'ft'),
            'duration_ref': (1.e3, 'ft'),
            'duration_bounds': ((200., 10.e3), 'ft'),
            'control_order': 1,
            'opt': True,
            'balance_throttle': False,
            'rotation': True,
            'constraints': {
                'normal_force': {
                    'equals': 0.,
                    'loc': 'final',
                    'units': 'lbf',
                    'type': 'boundary',
                    'ref': 10.e5,
                },
                # 'TAS': {
                #     'upper': 220.,
                #     'loc': 'final',
                #     'units': 'kn',
                #     'type': 'boundary',
                # },
            },
        },
        'subsystem_options': subsystem_options,
        'initial_guesses': {
            'distance': [(2.e3, 500.), 'ft'],
            'TAS': [(120., 130.), 'kn'],
            'time': [(20., 25.), 's'],
            'mass': [(175.e3-100., 175.e3-200.), 'lbm'],
            # 'altitude': [(0., 0.), 'ft'],
        },
    },
    'BC': {
        'user_options': {
            'num_segments': 5,
            'order': 3,
            'fix_initial': False,
            'throttle_setting': throttle_max,
            'input_speed_type': av.SpeedType.TAS,
            'ground_roll': False,
            'clean': False,
            'initial_ref': (1.e3, 'ft'),
            'initial_bounds': ((1., 16.e3), 'ft'),
            'duration_ref': (1.e3, 'ft'),
            'duration_bounds': ((500., 10.e3), 'ft'),
            'control_order': 1,
            'opt': True,
            'balance_throttle': False,
            'rotation': False,
            'constraints': {
                'flight_path_angle': {
                    'lower': 4.,
                    'loc': 'final',
                    'units': 'deg',
                    'type': 'boundary',
                },
                # 'TAS': {
                #     'equals': 150.,
                #     'loc': 'final',
                #     'units': 'kn',
                #     'type': 'boundary',
                #     'ref': 150.,
                # },

            },
        },
        'subsystem_options': subsystem_options,
        'initial_guesses': {
            'distance': [(2.5e3, 500.), 'ft'],
            'TAS': [(130., 130.), 'kn'],
            'time': [(25., 35.), 's'],
            'mass': [(175.e3-200., 175.e3-400.), 'lbm'],
            'altitude': [(0., 0.), 'ft'],
        },
    },
    'CD_to_P2': {
        'user_options': {
            'num_segments': 3,
            'order': 3,
            'fix_initial': False,
            'throttle_setting': throttle_max,
            'input_speed_type': av.SpeedType.TAS,
            'ground_roll': False,
            'clean': False,
            'initial_ref': (1.e3, 'ft'),
            'initial_bounds': ((1.e3, 20.e3), 'ft'),
            'duration_ref': (1.e3, 'ft'),
            'duration_bounds': ((150., 20.e3), 'ft'),
            'control_order': 1,
            'opt': True,
            'balance_throttle': False,
            'constraints': {
                'altitude': {
                    'lower': 100.,
                    'units': 'ft',
                    'type': 'boundary',
                    'loc': 'final',
                    'ref': 1000.,
                },
            },
        },
        'subsystem_options': subsystem_options,
        'initial_guesses': {
            'distance': [(3.e3, 10.e3), 'ft'],
            'time': [(35., 180.), 's'],
            'TAS': [(130., 130.), 'kn'],
            # 'mass': [(175.e3, 174.e3), 'lbm'],
            'altitude': [(0., 985.), 'ft'],
        },
    },
    # 'CD_past_P2': {
    #     'user_options': {
    #         'num_segments': 5,
    #         'order': 3,
    #         'fix_initial': False,
    #         'throttle_setting': throttle_climb,
    #         'input_speed_type': av.SpeedType.TAS,
    #         'ground_roll': False,
    #         'clean': False,
    #         'initial_ref': (1.e3, 'ft'),
    #         'initial_bounds': ((500., 60.e3), 'ft'),
    #         'duration_ref': (1.e3, 'ft'),
    #         'duration_bounds': ((150., 60.e3), 'ft'),
    #         'control_order': 1,
    #         'opt': True,
    #         'balance_throttle': False,
    #         'constraints': {
    #             'distance': {
    #                 'upper': 60.e3,
    #                 'units': 'ft',
    #                 'type': 'boundary',
    #                 'loc': 'final',
    #                 'ref': 30.e3,
    #             },
    #         },
    #     },
    #     'subsystem_options': subsystem_options,
    #     'initial_guesses': {
    #         'distance': [(15.e3, 20.e3), 'ft'],
    #         'time': [(120., 250.), 's'],
    #         'TAS': [(150., 150.), 'kn'],
    #         # 'mass': [(175.e3, 174.e3), 'lbm'],
    #         'altitude': [(985., 2000.), 'ft'],
    #     },
    # },
    # 'DE': {
    #     'user_options': {
    #         'num_segments': 3,
    #         'order': 3,
    #         'fix_initial': False,
    #         'throttle_setting': throttle_climb,
    #         'input_speed_type': av.SpeedType.TAS,
    #         'ground_roll': False,
    #         'clean': False,
    #         'initial_ref': (1.e3, 'ft'),
    #         'initial_bounds': ((500., 2500.), 'ft'),
    #         'duration_ref': (1.e3, 'ft'),
    #         'duration_bounds': ((50., 2000.), 'ft'),
    #         'control_order': 1,
    #         'opt': True,
    #         'constraints': {
    #             'distance': {
    #                 'upper': 19000.,
    #                 'units': 'ft',
    #                 'type': 'boundary',
    #                 'loc': 'final',
    #             },
    #         },
    #     },
    #     'subsystem_options': subsystem_options,
    #     'initial_guesses': {
    #         'distance': [(1000., 2000.), 'ft'],
    #         'TAS': [(100., 150.), 'kn'],
    #         'mass': [(175.e3, 174.e3), 'lbm'],
    #         'altitude': [(0., 1000.), 'ft'],
    #     },
    # 'EF_to_P1': {
    #     'user_options': {
    #         'num_segments': 3,
    #         'order': 3,
    #         'fix_initial': False,
    #         'throttle_setting': throttle_climb,
    #         'input_speed_type': av.SpeedType.TAS,
    #         'ground_roll': False,
    #         'clean': False,
    #         'initial_ref': (1.e3, 'ft'),
    #         'initial_bounds': ((500., 2500.), 'ft'),
    #         'duration_ref': (1.e3, 'ft'),
    #         'duration_bounds': ((50., 2000.), 'ft'),
    #         'control_order': 1,
    #         'opt': True,
    #         'constraints': {
    #             'distance': {
    #                 'equals': 21325.,
    #                 'units': 'ft',
    #                 'type': 'boundary',
    #                 'loc': 'final',
    #             },
    #         },
    #     },
    #     'subsystem_options': subsystem_options,
    #     'initial_guesses': {
    #         'distance': [(1000., 2000.), 'ft'],
    #         'TAS': [(100., 150.), 'kn'],
    #         'mass': [(175.e3, 174.e3), 'lbm'],
    #         'altitude': [(0., 1000.), 'ft'],
    #     },
    # 'EF_past_P1': {
    #     'user_options': {
    #         'num_segments': 3,
    #         'order': 3,
    #         'fix_initial': False,
    #         'throttle_setting': throttle_climb,
    #         'input_speed_type': av.SpeedType.TAS,
    #         'ground_roll': False,
    #         'clean': False,
    #         'initial_ref': (1.e3, 'ft'),
    #         'initial_bounds': ((500., 2500.), 'ft'),
    #         'duration_ref': (1.e3, 'ft'),
    #         'duration_bounds': ((50., 2000.), 'ft'),
    #         'control_order': 1,
    #         'opt': True,
    #         'constraints': {
    #         },
    #     },
    #     'subsystem_options': subsystem_options,
    #     'initial_guesses': {
    #         'distance': [(1000., 2000.), 'ft'],
    #         'TAS': [(100., 150.), 'kn'],
    #         'mass': [(175.e3, 174.e3), 'lbm'],
    #         'altitude': [(0., 1000.), 'ft'],
    #     },
    # },
    "post_mission": {
        "include_landing": False,
        "constrain_range": False,
        "target_range": (1906, "nmi"),
    },
}


prob = av.AviaryProblem()

# Load aircraft and options data from user
# Allow for user overrides here
prob.load_inputs('models/test_aircraft/playground.csv', phase_info)


# Preprocess inputs
prob.check_and_preprocess_inputs()

prob.add_pre_mission_systems()

prob.add_phases()

prob.add_post_mission_systems()

# Link phases and variables
prob.link_phases()

prob.add_driver("SNOPT", max_iter=50)

prob.add_design_variables()

# Load optimization problem formulation
# Detail which variables the optimizer can control
prob.add_objective('fuel_burned')

prob.setup()

prob.set_initial_guesses()

prob.run_aviary_problem()

# prob.model.list_inputs(units=True, print_arrays=True)
# prob.model.list_outputs(units=True, print_arrays=True)
