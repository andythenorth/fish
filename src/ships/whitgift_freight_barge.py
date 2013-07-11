from ship import Ship

ship = Ship(id = 'whitgift_freight_barge',
            numeric_id = '160', 
            capacity_cargo_holds = 55, 
            capacity_tanks = 0, 
            replacement_id = '-none', 
            fixed_run_cost_factor = 1.0, 
            supertype = 'gcv', 
            speed = 18.0, 
            speed_factor_unladen = 1.1, 
            title = 'Whitgift [Freight Barge]', 
            inland_capable = True, 
            offsets = [[-14, -40], [-78, -21], [-68, -21], [-30, -21], [-14, -40], [-78, -24], [-68, -21], [-32, -21]], 
            buy_menu_width = 44, 
            capacity_freight = 55, 
            loading_speed = '20', 
            capacity_pax = 0, 
            intro_date = 1870, 
            buy_menu_bb_xy = [667, 21], 
            graphic_variations_by_date = [[[0, 9999]], {0: [0]}], 
            graphics_template = 'standard_gcv', 
            str_type_info = 'SMALL_FREIGHTER_COASTAL_INLAND', 
            sea_capable = True, 
            fuel_run_cost_factor = 1.0, 
            buy_cost = 4, 
            capacity_special = [], 
            vehicle_life = 60, 
            capacity_mail = 0, 
            custom_template = None, 
            gross_tonnage = 60, 
            default_cargo = 'COAL', 
)