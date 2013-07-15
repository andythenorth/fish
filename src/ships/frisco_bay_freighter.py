from ship import Ship, GeneralCargoVessel

ship = GeneralCargoVessel(id = 'frisco_bay_freighter',
            numeric_id = 220,
            title = 'Frisco Bay [Freighter]',
            capacity_pax = 0,
            capacity_cargo_holds = 810,
            capacity_mail = 0,
            capacity_special = [],
            replacement_id = '-none',
            buy_cost = 58,
            fixed_run_cost_factor = 10.0,
            fuel_run_cost_factor = 1.0,
            speed = 18.0,
            speed_factor_unladen = 1.1,
            inland_capable = False,
            sea_capable = True,
            offsets = [[-14, -42], [-61, -28], [-55, -29], [-10, -28], [-14, -54], [-61, -28], [-55, -29], [-9, -28]],
            buy_menu_width = 119,
            loading_speed = 20,
            intro_date = 1915,
            buy_menu_bb_xy = [620, 28],
            graphic_variations_by_date = [[[0, 9999]], {0: [0]}],
            str_type_info = 'LARGE_COASTER',
            vehicle_life = 35,
            gross_tonnage = 820,
)
