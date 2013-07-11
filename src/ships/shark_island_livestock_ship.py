from ship import Ship

ship = Ship(id = 'shark_island_livestock_ship',
            numeric_id = '290',
            capacity_cargo_holds = 0,
            capacity_tanks = 0,
            replacement_id = '-none',
            fixed_run_cost_factor = 10.0,
            supertype = 'livestock_ship',
            speed = 26.0,
            speed_factor_unladen = 1.1,
            title = 'Shark Island [Livestock Ship]',
            inland_capable = False,
            offsets = [[-14, -42], [-61, -28], [-55, -29], [-10, -28], [-14, -54], [-61, -28], [-55, -29], [-9, -28]],
            buy_menu_width = 119,
            capacity_freight = 0,
            loading_speed = '20',
            capacity_pax = 0,
            intro_date = 1960,
            buy_menu_bb_xy = [620, 28],
            graphic_variations_by_date = [[[0, 9999]], {0: [0]}],
            graphics_template = 'standard_gcv',
            str_type_info = 'LIVESTOCK_SHIP',
            sea_capable = True,
            fuel_run_cost_factor = 1.0,
            buy_cost = 58,
            capacity_special = [200, 400, 600],
            vehicle_life = 35,
            capacity_mail = 0,
            custom_template = None,
            gross_tonnage = 650,
            default_cargo = 'LVST',
)
