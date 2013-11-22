import global_constants
from ship import Ship, PacketBoat

ship = PacketBoat(id = 'castle_point_steamer',
            numeric_id = 30,
            title = 'Castle Point [Steamer]',
            capacity_pax = 400,
            capacity_cargo_holds = 250,
            capacity_mail = 320,
            replacement_id = '-none',
            buy_cost = 27,
            fixed_run_cost_factor = 5.0,
            fuel_run_cost_factor = 1.0,
            speed = 25.0,
            speed_factor_unladen = 1.0,
            inland_capable = False,
            sea_capable = True,
            offsets = [[-14, -54], [-61, -28], [-36, -29], [-10, -28], [-14, -54], [-55, -26], [-36, -29], [0, -24]],
            buy_menu_width = 94,
            loading_speed = 20,
            intro_date = 1900,
            buy_menu_bb_xy = [645, 28],
            str_type_info = 'FAST_PACKET_STEAMER',
            vehicle_life = 25,
            gross_tonnage = 460,
            vehicle_groups = ['sea'], 
            graphics_status = 'Work in Progress - Coxx',)

ship.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
