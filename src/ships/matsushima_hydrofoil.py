from ship import Ship, PassengerMailFerry

ship = PassengerMailFerry(id = 'matsushima_hydrofoil',
            numeric_id = '70',
            title = 'Matsushima [Hydrofoil]',
            capacity_pax = 240,
            capacity_freight = 0,
            capacity_cargo_holds = 0,
            capacity_tanks = 0,
            capacity_mail = 60,
            capacity_special = [],
            default_cargo = 'PASS',
            replacement_id = '-none',
            buy_cost = 44,
            fixed_run_cost_factor = 6.0,
            fuel_run_cost_factor = 3.5,
            speed = 56.0,
            speed_factor_unladen = 1.0,
            inland_capable = False,
            sea_capable = True,
            offsets = [[-14, -54], [-57, -26], [-35, -29], [-19, -32], [-14, -54], [-58, -32], [-42, -29], [-1, -26]],
            buy_menu_width = 67,
            loading_speed = '18',
            intro_date = 1978,
            buy_menu_bb_xy = [624, 28],
            graphic_variations_by_date = [[[0, 9999]], {0: [0]}],
            graphics_template = 'hydrofoil',
            str_type_info = 'HYDROFOIL_FAST_FERRY',
            vehicle_life = 45,
            custom_template = None,
            gross_tonnage = 120,
)
