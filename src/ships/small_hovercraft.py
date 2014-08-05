import global_constants
from ship import Ship, PacketBoat

ship = PacketBoat(id = 'small_hovercraft',
            numeric_id = 150,
            title = 'Small [Hovercraft]',
            capacity_pax = 70,
            capacity_cargo_holds = 25,
            capacity_mail = 30,
            replacement_id = '-none',
            buy_cost = 24,
            fixed_run_cost_factor = 3.0,
            fuel_run_cost_factor = 8.0,
            speed = 70.0,
            speed_factor_unladen = 1.3,
            inland_capable = True,
            sea_capable = True,
            offsets = [[-14, -40], [-82, -24], [-69, -21], [-29, -24], [-14, -42], [-80, -26], [-68, -21], [-29, -24]],
            buy_menu_width = 42,
            loading_speed = 30,
            intro_date = 1965,
            buy_menu_bb_xy = [668, 21],
            str_type_info = 'HOVERCRAFT_FAST_FERRY',
            vehicle_life = 45,
            gross_tonnage = 30,
            graphics_status = 'Done',)

ship.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
