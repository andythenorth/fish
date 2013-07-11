from ship import Ship

ship = Ship(id = 'castle_point_steamer',
            numeric_id = '30', 
            capacity_cargo_holds = 250, 
            capacity_tanks = 0, 
            replacement_id = '-none', 
            fixed_run_cost_factor = 5.0, 
            supertype = 'packet', 
            speed = 25.0, 
            speed_factor_unladen = 25.0, 
            title = 'Castle Point [Steamer]', 
            inland_capable = False, 
            offsets = [[-14, -54], [-61, -28], [-36, -29], [-10, -28], [-14, -54], [-55, -26], [-36, -29], [0, -24]], 
            buy_menu_width = 89, 
            capacity_freight = 250, 
            loading_speed = '30', 
            capacity_pax = 400, 
            intro_date = 1900, 
            buy_menu_bb_xy = [622, 28], 
            graphic_variations_by_date = [[[0, 9999]], {0: [0]}], 
            graphics_template = 'default', 
            str_type_info = 'FAST_PACKET_STEAMER', 
            sea_capable = True, 
            fuel_run_cost_factor = 1.0, 
            buy_cost = 27, 
            capacity_special = [], 
            vehicle_life = 25, 
            capacity_mail = 320, 
            custom_template = None, 
            gross_tonnage = 460, 
            default_cargo = 'PASS', 
)