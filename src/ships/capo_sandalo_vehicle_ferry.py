from ship import Ship

ship = Ship(id = 'capo_sandalo_vehicle_ferry',
            numeric_id = '80',
            capacity_pax = 1000,
            capacity_freight = 470,
            capacity_cargo_holds = 470,
            capacity_tanks = 0,
            capacity_mail = 720,
            capacity_special = [],
            replacement_id = '-none',
            fixed_run_cost_factor = 16.0,
            supertype = 'packet',
            speed = 23.0,
            speed_factor_unladen = 1.0,
            title = 'Capo Sandalo [Ferry]',
            inland_capable = False,
            offsets = [[-14, -41], [-67, -25], [-59, -29], [-15, -26], [-14, -45], [-67, -26], [-59, -29], [-15, -25]],
            buy_menu_width = 117,
            loading_speed = '30',
            intro_date = 1959,
            buy_menu_bb_xy = [620, 28],
            graphic_variations_by_date = [[[0, 9999]], {0: [0]}],
            graphics_template = 'default',
            str_type_info = 'VEHICLE_FERRY',
            sea_capable = True,
            fuel_run_cost_factor = 1.0,
            buy_cost = 63,
            vehicle_life = 45,
            custom_template = None,
            gross_tonnage = 1150,
            default_cargo = 'PASS',
)
