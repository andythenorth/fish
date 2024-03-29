import global_constants
from ship import PacketBoat

ship = PacketBoat(id = 'danube_large_ferry',
            numeric_id = 2030,
            title = 'DANUBE LARGE [Ferry]',
            capacity_pax = 1000,
            capacity_cargo_holds = 450,
            capacity_mail = 600,
            replacement_id = '-none',
            buy_cost = 27,
            fixed_run_cost_factor = 5.0,
            fuel_run_cost_factor = 1.0,
            speed = 30.0,
            speed_factor_unladen = 1.0,
            inland_capable = True,
            sea_capable = True,
            offsets = [[-14, -47], [-73, -22], [-57, -29], [-20, -22], [-14, -47], [-73, -22], [-57, -29], [-20, -22]],
            buy_menu_width = 116,
            loading_speed = 30,
            intro_date = 1960,
            buy_menu_bb_xy = [620, 28],
            str_type_info = 'VEHICLE_FERRY',
            vehicle_life = 40,
            gross_tonnage = 60)

ship.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
