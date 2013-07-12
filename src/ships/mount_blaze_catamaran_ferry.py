from ship import Ship

ship = Ship(id = 'mount_blaze_catamaran_ferry',
            numeric_id = '100',
            capacity_pax = 1600,
            capacity_freight = 450,
            capacity_cargo_holds = 450,
            capacity_tanks = 0,
            capacity_mail = 630,
            capacity_special = [],
            replacement_id = '-none',
            buy_cost = 63,
            fixed_run_cost_factor = 16.0,
            fuel_run_cost_factor = 1.0,
            supertype = 'packet',
            speed = 40.0,
            speed_factor_unladen = 1.0,
            title = 'Mount Blaze [Fast Ferry]',
            inland_capable = False,
            offsets = [[-14, -41], [-67, -25], [-59, -29], [-15, -26], [-14, -45], [-67, -26], [-59, -29], [-15, -25]],
            buy_menu_width = 117,
            loading_speed = '20',
            intro_date = 2002,
            buy_menu_bb_xy = [620, 28],
            graphic_variations_by_date = [[[0, 9999]], {0: [0]}],
            graphics_template = 'default',
            str_type_info = 'CATAMARAN_FAST_FERRY',
            sea_capable = True,
            vehicle_life = 30,
            custom_template = None,
            gross_tonnage = 1800,
            default_cargo = 'PASS',
)
