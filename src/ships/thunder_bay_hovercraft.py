from ship import Ship

ship = Ship(id = 'thunder_bay_hovercraft',
            numeric_id = '150',
            capacity_pax = 0,
            capacity_freight = 30,
            capacity_cargo_holds = 30,
            capacity_tanks = 0,
            capacity_mail = 30,
            capacity_special = [],
            replacement_id = '-none',
            fixed_run_cost_factor = 3.0,
            supertype = 'fast_freighter',
            speed = 46.0,
            speed_factor_unladen = 1.3,
            title = 'Thunder Bay [Hovercraft]',
            inland_capable = True,
            offsets = [[-14, -40], [-82, -24], [-69, -21], [-29, -24], [-14, -42], [-80, -26], [-68, -21], [-29, -24]],
            buy_menu_width = 39,
            loading_speed = '30',
            intro_date = 1972,
            buy_menu_bb_xy = [654, 21],
            graphic_variations_by_date = [[[0, 9999]], {0: [0]}],
            graphics_template = '2_visible_cargo_states',
            str_type_info = 'CARGO_HOVERCRAFT',
            sea_capable = True,
            fuel_run_cost_factor = 8.0,
            buy_cost = 24,
            vehicle_life = 45,
            custom_template = None,
            gross_tonnage = 30,
            default_cargo = 'GOOD',
)
