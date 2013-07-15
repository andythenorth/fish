from ship import Ship, LogTug

ship = LogTug(id = 'pine_island_log_tug',
            numeric_id = 250,
            title = 'Pine Island [Log Tug]',
            capacity_pax = 0,
            capacity_freight = 0,
            capacity_cargo_holds = 0,
            capacity_tanks = 0,
            capacity_mail = 0,
            capacity_special = [80, 240, 400],
            default_cargo = 'WOOD',
            replacement_id = '-none',
            buy_cost = 4,
            fixed_run_cost_factor = 2.0,
            fuel_run_cost_factor = 1.0,
            speed = 12.0,
            speed_factor_unladen = 1.7,
            inland_capable = False,
            sea_capable = True,
            offsets = [[0, 0]],
            buy_menu_width = 24,
            loading_speed = '20',
            intro_date = 1900,
            buy_menu_bb_xy = [620, 28],
            graphic_variations_by_date = [[[0, 9999]], {0: [0]}],
            graphics_template = 'default',
            str_type_info = 'LOG_TUG',
            vehicle_life = 25,
            gross_tonnage = 26,
)
