from roster import Roster

#from ships import altamira_freighter
#from ships import barletta_paddle_steamer
#from ships import cadiz_freighter
#from ships import cape_spear_trawler
#from ships import castle_point_steamer
from ships import constance_freight_barge
from ships import danube_large_ferry
from ships import danube_livestock_barge
from ships import danube_paddle_steamer
from ships import danube_reefer
from ships import danube_small_ferry
from ships import dieze_container_barge
#from ships import eddystone_tanker
#from ships import fish_island_trawler
#from ships import frisco_bay_freighter
from ships import feodosiya_hydrofoil
from ships import geneva_freight_barge
#from ships import harbour_point_utility_vessel
#from ships import hopetown_tanker
#from ships import hovercraft_pax_large
#from ships import marstein_freighter
#from ships import maspalomas_freighter
#from ships import santorini_freighter
from ships import saint_marie_barge_tug
#from ships import shark_island_livestock_ship
#from ships import sunk_rock_ferry
from ships import volgoneft_six_thirty_tanker_barge
from ships import volgoneft_two_seventy_tanker_barge
#from ships import whitgift_freight_barge
#from ships import yokohama_tanker

roster = Roster(id = 'euro',
                buy_menu_sort_order = [#'harbour_point_utility_vessel',
                                       'danube_small_ferry',
                                       'danube_paddle_steamer',
                                       'danube_large_ferry',
                                       'feodosiya_hydrofoil',
                                       #'fish_island_trawler',
                                       #'cape_spear_trawler',
                                       #'whitgift_freight_barge',
                                       #'marstein_freighter',
                                       #'altamira_freighter',
                                       'saint_marie_barge_tug',
                                       'constance_freight_barge',
                                       'geneva_freight_barge',
                                       #'cadiz_freighter',
                                       #'frisco_bay_freighter',
                                       #'santorini_freighter',
                                       #'maspalomas_freighter',
                                       #'eddystone_tanker',
                                       #'hopetown_tanker',
                                       #'yokohama_tanker',
                                       'volgoneft_two_seventy_tanker_barge',
                                       'volgoneft_six_thirty_tanker_barge',
                                       'danube_reefer',
                                       'danube_livestock_barge',
                                       'dieze_container_barge'])
