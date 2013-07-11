from ship import Ship

ship = Ship(id = 'little_cumbrae_freighter',
            numeric_id = '180', 
            capacity_cargo_holds = 160, 
            capacity_tanks = 0, 
            replacement_id = '-none', 
            fixed_run_cost_factor = 2.0, 
            supertype = 'gcv', 
            speed = 18.0, 
            speed_factor_unladen = 1.1, 
            title = 'Little Cumbrae [Freighter]', 
            inland_capable = True, 
            offsets = [[-14, -40], [-80, -24], [-66, -21], [-33, -25], [-14, -40], [-78, -26], [-66, -21], [-32, -23]], 
            buy_menu_width = 78, 
            capacity_freight = 160, 
            loading_speed = '20', 
            capacity_pax = 0, 
            intro_date = 1870, 
            buy_menu_bb_xy = [649, 21], 
            graphic_variations_by_date = [[[0, 1952], [1950, 9999]], {0: [0], 1952: [1], 1950: [0, 1]}], 
            graphics_template = 'standard_gcv', 
            str_type_info = 'SMALL_FREIGHTER_COASTAL_INLAND', 
            sea_capable = True, 
            fuel_run_cost_factor = 1.0, 
            buy_cost = 12, 
            capacity_special = [], 
            vehicle_life = 35, 
            capacity_mail = 0, 
            custom_template = None, 
            gross_tonnage = 100, 
            default_cargo = 'COAL', 
)