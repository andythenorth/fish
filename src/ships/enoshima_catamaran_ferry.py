from ship import Ship

ship = Ship(id = 'enoshima_catamaran_ferry',
            numeric_id = '90', 
            capacity_cargo_holds = 175, 
            capacity_tanks = 0, 
            replacement_id = '-none', 
            fixed_run_cost_factor = 16.0, 
            supertype = 'packet', 
            speed = 50.0, 
            speed_factor_unladen = 50.0, 
            title = 'Enoshima [Fast Ferry]', 
            inland_capable = False, 
            offsets = [[-14, -54], [-57, -26], [-35, -29], [-19, -32], [-14, -54], [-58, -32], [-42, -29], [-1, -26]], 
            buy_menu_width = 67, 
            capacity_freight = 175, 
            loading_speed = '20', 
            capacity_pax = 300, 
            intro_date = 1997, 
            buy_menu_bb_xy = [624, 28], 
            graphic_variations_by_date = [[[1997, 9999], [1997, 9999]], {1997: [0, 1]}], 
            graphics_template = 'default', 
            str_type_info = 'CATAMARAN_FAST_FERRY', 
            sea_capable = True, 
            fuel_run_cost_factor = 1.0, 
            buy_cost = 63, 
            capacity_special = [], 
            vehicle_life = 25, 
            capacity_mail = 224, 
            custom_template = None, 
            gross_tonnage = 350, 
            default_cargo = 'PASS', 
)