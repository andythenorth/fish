from ship import Ship

ship = Ship(id = 'santorini_freighter',
            numeric_id = '230',
            capacity_pax = 0,
            capacity_freight = 960,
            capacity_cargo_holds = 960,
            capacity_tanks = 0,
            capacity_mail = 0,
            capacity_special = [],
            replacement_id = '-none',
            fixed_run_cost_factor = 7.0,
            supertype = 'gcv',
            speed = 20.0,
            speed_factor_unladen = 1.1,
            title = 'Santorini [Freighter]',
            inland_capable = False,
            offsets = [[-14, -41], [-74, -22], [-65, -29], [-21, -22], [-14, -45], [-75, -22], [-65, -29], [-20, -22]],
            buy_menu_width = 138,
            loading_speed = '20',
            intro_date = 1953,
            buy_menu_bb_xy = [620, 28],
            graphic_variations_by_date = [[[0, 1974], [1953, 9999]], {0: [0], 1953: [0, 1], 1974: [1]}],
            graphics_template = 'standard_gcv',
            str_type_info = 'LARGE_COASTER',
            sea_capable = True,
            fuel_run_cost_factor = 1.0,
            buy_cost = 85,
            vehicle_life = 35,
            custom_template = None,
            gross_tonnage = 960,
            default_cargo = 'COAL',
)
