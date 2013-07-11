from ship import Ship

ship = Ship(id = 'feodosiya_hydrofoil',
            numeric_id = '60', 
            capacity_cargo_holds = 0, 
            capacity_tanks = 0, 
            replacement_id = '-none', 
            fixed_run_cost_factor = 5.0, 
            supertype = 'pax_mail', 
            speed = 40.0, 
            speed_factor_unladen = 40.0, 
            title = 'Feodosiya [Hydrofoil]', 
            inland_capable = True, 
            offsets = [[-14, -59], [-58, -32], [-36, -31], [-17, -32], [-14, -58], [-55, -26], [-39, -29], [0, -24]], 
            buy_menu_width = 64, 
            capacity_freight = 0, 
            loading_speed = '15', 
            capacity_pax = 106, 
            intro_date = 1967, 
            buy_menu_bb_xy = [625, 28], 
            graphic_variations_by_date = [[[0, 9999]], {0: [0]}], 
            graphics_template = 'hydrofoil', 
            str_type_info = 'HYDROFOIL_FAST_FERRY', 
            sea_capable = True, 
            fuel_run_cost_factor = 3.0, 
            buy_cost = 28, 
            capacity_special = [], 
            vehicle_life = 35, 
            capacity_mail = 32, 
            custom_template = None, 
            gross_tonnage = 64, 
            default_cargo = 'PASS', 
)