from rosters import registered_rosters


class Roster(object):
    """
    Rosters compose a set of vehicles which is complete for gameplay.
    """
    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.ships = []
        for ship in [ship.ship for ship in kwargs.get('ships')]:
            self.ships.append(ship)
            ship.roster_id = self.id

    @property
    def buy_menu_sort_order(self):
        return [ship.id for ship in self.ships]

    def register(roster):
        registered_rosters.append(roster)
