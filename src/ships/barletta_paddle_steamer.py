from ship import Ship, PacketBoat

ship = PacketBoat(id = 'barletta_paddle_steamer',
            numeric_id = '20',
            supertype = 'packet',
            title = 'Barletta [Paddle Steamer]',
            capacity_pax = 248,
            capacity_freight = 96,
            capacity_cargo_holds = 96,
            capacity_tanks = 0,
            capacity_mail = 120,
            capacity_special = [],
            default_cargo = 'PASS',
            replacement_id = 'patos_island_vehicle_ferry',
            buy_cost = 32,
            fixed_run_cost_factor = 9.0,
            fuel_run_cost_factor = 1.0,
            speed = 23.0,
            speed_factor_unladen = 1.0,
            inland_capable = True,
            sea_capable = True,
            offsets = [[-14, -54], [-63, -24], [-50, -29], [-10, -28], [-14, -55], [-58, -27], [-50, -29], [-8, -24]],
            buy_menu_width = 89,
            loading_speed = '12',
            intro_date = 1870,
            buy_menu_bb_xy = [626, 26],
            graphic_variations_by_date = [[[0, 9999]], {0: [0]}],
            graphics_template = 'default',
            str_type_info = 'PADDLE_STEAMER',
            vehicle_life = 40,
            custom_template = None,
            gross_tonnage = 280,
)
