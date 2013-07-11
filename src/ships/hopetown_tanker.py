from ship import Ship

ship = Ship(id = 'hopetown_tanker',
            numeric_id = '270',
            capacity_cargo_holds = 0,
            capacity_tanks = 770,
            capacity_mail = 0,
            capacity_special = [],
            replacement_id = '-none',
            fixed_run_cost_factor = 12.0,
            supertype = 'tanker',
            speed = 20.0,
            speed_factor_unladen = 1.1,
            title = 'Hopetown [Tanker]',
            inland_capable = False,
            offsets = [[-14, -42], [-61, -28], [-55, -29], [-10, -28], [-14, -54], [-61, -28], [-55, -29], [-9, -28]],
            buy_menu_width = 114,
            capacity_freight = 770,
            loading_speed = '40',
            capacity_pax = 0,
            intro_date = 1926,
            buy_menu_bb_xy = [620, 28],
            graphic_variations_by_date = [[[0, 9999]], {0: [0]}],
            graphics_template = 'tanker',
            str_type_info = 'COASTAL_TANKER',
            sea_capable = True,
            fuel_run_cost_factor = 1.1000000000000001,
            buy_cost = 64,
            vehicle_life = 45,
            custom_template = None,
            gross_tonnage = 800,
            default_cargo = 'OIL_',
)
