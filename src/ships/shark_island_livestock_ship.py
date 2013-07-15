from ship import Ship, LivestockCarrier

ship = LivestockCarrier(id = 'shark_island_livestock_ship',
            numeric_id = 290,
            title = 'Shark Island [Livestock Ship]',
            capacity_pax = 0,
            capacity_freight = 0,
            capacity_cargo_holds = 0,
            capacity_tanks = 0,
            capacity_mail = 0,
            capacity_special = [200, 400, 600],
            default_cargo = 'LVST',
            replacement_id = '-none',
            buy_cost = 58,
            fixed_run_cost_factor = 10.0,
            fuel_run_cost_factor = 1.0,
            speed = 26.0,
            speed_factor_unladen = 1.1,
            inland_capable = False,
            sea_capable = True,
            offsets = [[-14, -42], [-61, -28], [-55, -29], [-10, -28], [-14, -54], [-61, -28], [-55, -29], [-9, -28]],
            buy_menu_width = 119,
            loading_speed = '20',
            intro_date = 1960,
            buy_menu_bb_xy = [620, 28],
            graphic_variations_by_date = [[[0, 9999]], {0: [0]}],
            graphics_template = 'standard_gcv',
            str_type_info = 'LIVESTOCK_SHIP',
            vehicle_life = 35,
            custom_template = None,
            gross_tonnage = 650,
)
