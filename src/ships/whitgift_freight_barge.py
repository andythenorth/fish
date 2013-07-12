from ship import Ship

ship = Ship(id = 'whitgift_freight_barge',
            numeric_id = '160',
            supertype = 'gcv',
            title = 'Whitgift [Freight Barge]',
            capacity_freight = 55,
            capacity_pax = 0,
            capacity_cargo_holds = 55,
            capacity_tanks = 0,
            capacity_mail = 0,
            capacity_special = [],
            default_cargo = 'COAL',
            replacement_id = '-none',
            buy_cost = 4,
            fixed_run_cost_factor = 1.0,
            fuel_run_cost_factor = 1.0,
            speed = 18.0,
            speed_factor_unladen = 1.1,
            inland_capable = True,
            sea_capable = True,
            offsets = [[-14, -40], [-78, -21], [-68, -21], [-30, -21], [-14, -40], [-78, -24], [-68, -21], [-32, -21]],
            buy_menu_width = 44,
            loading_speed = '20',
            intro_date = 1870,
            buy_menu_bb_xy = [667, 21],
            graphic_variations_by_date = [[[0, 9999]], {0: [0]}],
            graphics_template = 'standard_gcv',
            str_type_info = 'SMALL_FREIGHTER_COASTAL_INLAND',
            vehicle_life = 60,
            custom_template = None,
            gross_tonnage = 60,
)
