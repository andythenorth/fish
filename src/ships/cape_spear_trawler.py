from ship import Ship, Trawler

ship = Trawler(id = 'cape_spear_trawler',
            numeric_id = 140,
            title = 'Cape Spear [Trawler]',
            capacity_pax = 40,
            capacity_freight = 44,
            capacity_cargo_holds = 44,
            capacity_tanks = 0,
            capacity_mail = 66,
            capacity_special = [84],
            replacement_id = '-none',
            buy_cost = 6,
            fixed_run_cost_factor = 2.0,
            fuel_run_cost_factor = 1.0,
            speed = 16.0,
            speed_factor_unladen = 1.15,
            inland_capable = True,
            sea_capable = True,
            offsets = [[-14, -40], [-78, -21], [-68, -21], [-30, -21], [-14, -40], [-78, -24], [-68, -21], [-32, -21]],
            buy_menu_width = 51,
            loading_speed = '15',
            intro_date = 1870,
            buy_menu_bb_xy = [663, 21],
            graphic_variations_by_date = [[[0, 9999]], {0: [0]}],
            graphics_template = 'default',
            str_type_info = 'TRAWLER',
            vehicle_life = 40,
            gross_tonnage = 84,
)
