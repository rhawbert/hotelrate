from json import dumps
from random import choice, randrange

from flask import Flask, Response

app = Flask(__name__)

WHAT = ('desk', 'nightstand', 'minibar', 'ac', 'table', 'shower', 'lavatory',
        'toilet', 'balcony', 'window', 'couch', 'chair')


def gen_severity():
    mapping = {
        1: 'Incidental',
        2: 'Minor',
        3: 'Moderate',
        4: 'Major',
        5: 'Business Threatening'
    }
    key = choice(list(mapping.keys()))
    return {
        'id': key,
        'description': mapping[key]
    }


def gen_category():
    mapping = {
        1: 'Cleanliness',
        2: 'Organizational',
        3: 'Legal',
        4: 'Health',
        5: 'Staff'
    }
    key = choice(list(mapping.keys()))
    return {
        'id': key,
        'description': mapping[key]
    }


def gen_where():
    where = ('room', 'suite', 'penthouse', 'hall', 'lobby', 'kitchen')
    output = choice(where)
    if output in ('room', 'suite', 'penthouse'):
        number = "{}{:02d}".format(randrange(1, 21), randrange(1, 21))
        output += number
    return output


def gen_rules():
    rules = (
        'All debris/trash should be removed from surface',
        'Cat smells',
        'Permanent sag or dent in mattress',
        'Car, truck taxi, motorcyle noise, and traffic',
        'Receptionist playing music or do annoying behavior',
        'Unhelpful staff',
        'Animals, Dog, Cats and Chickens',
        'Construction working being done at hotel or close.',
        'Churches, Mosques Make Noise',
        'No Electricity or Brown Outs, without generator backup.',
        'Floor Fan is Missing Plug',
        'Floor Fan is Broken',
        'Noise coming from plumbing or sanitary pipes as water comes down from upper floors.',
        'Fan in Center of Ceiling too Slow',
        'Fan in Center of Ceiling does not Work',
        'Fan in Center of Ceiling only has one speed',
        'Fan in Center of Ceiling Squeaks',
        'Light Bulbs Burned Out',
        'Transom Above Door is Screen and Noise is Loud',
        'Rock and Roll Bands',
        'Staff steals when cleaning the room',
        'Overcharged',
        'Ants',
        'Mosquitoes',
        'No Mosquito Net',
        'Spiders',
        'Mice or Rats',
        'Cockroaches',
        'No labels on hot or cold water, there is no way to know on or off.',
        'Furniture is in wrong location.',
        'Never offer to clean the room or change the sheets.',
        'Construction for hotel started during high season.',
        'Construction project in streets in front of hotel.',
        'You can hear constructon projects from neighbors.',
        'The problems above, should disappear at higher price levels, or maybe you are paying too much.',
        'Tour Buses with Large Groups Making Noise',
        'Unhelpful staff',
        'No fresh air because of air conditioning and you have sinus or breathing problems.',
        'No way to wash clothes and none provided',
        'Courtyard windows facing so you can hear TV, People in other rooms',
        'Maintenance Never Done',
        'Air Conditioners Blows directly at Bed or Eyes of person sleeping',
        'Air Conditioner is Noisy',
        'Plumbing Traps missing on Sink or Shower Drains',
        'Tourist Traps that are too close',
        'Group Rents the complete Hotel and makes noise or you have to move.',
        'Ceiling is too High and Air Conditioner does not Cool Room',
        'Remote Control on Televisions does not work',
        'No security box big enough for computer or camera.',
        'No booking on arrival or Overbooked',
        'WIFI or Internet Access only in Common Areas',
        'There is No Sign to Hang on Door Requesting Room to be Cleaned',
        'No security box big enough for computer or camera.',
        'Staff steals when cleaning the room',
        'Tour sales people hanging, or waiting for you to leave in front of Hotel',
        'Housecleaning ignores signs, and clean room when sign posted to not clean.',
        'Tourist Traps that are too close',
        'Staff is indifferent and non-caring',
        'Too far from infrastructure of city',
        'No fresh air because of type of air conditioning, and you have sinus or breathing problems.',
        'No way to wash clothes and none provided.',
        'Bums - Beggars Waiting or Hanging out in front of Hotel',
        'WIFI or Internet Access only in Common Areas, or you need to pay.',
        'No security box big enough for computer or camera.',
        'Taxis are Overpriced just outside door to Hotel and no way to get proper priced Tax',
        'Staff is Indifferent and Non-Caring',
        'No fresh air because of air conditioning and you have sinus or breathing problems.',
        'No Scales to Weigh Luggage',
        'WIFI or Internet Access only in Common Areas',
        'Overcharged',
        'Taxis are Overpriced just outside door to Hotel and no way to get proper priced Taxi',
        'Remote Control on Televisions does not work',
        'Mini bar scam',
        'Hotel Occupied by One Culture or Country and Dominate',
        'Staff Does Not Arrange Taxis',
        'Sub Standard restaurant',
        'Inaccurate star rating',
        'No Scales to Weigh Luggage',
        'No Health Center or Not Open at Sufficient Hours',
        'No security box big enough for computer or camera.',
        'No Prices on Services',
        'Overcharged',
        'Remote Control on Televisions does not work',
        'Taxis are Overpriced just outside door to Hotel and no way to get proper priced Taxi',
        'You assumed more money was better.',
        'The Internet is extra charge and the cost is extremely expensive.',
        'Hotel Occupied by One Culture or Country and Dominate',
        'Overcharged',
        'Mini bar scam',
        'Sub Standard restaurant',
        'Women are told they cannot be Topless',
        'Inaccurate star rating',
        'People are too Old to be Fun',
        'Business Center People are not Educated Sufficiently',
        'No Health Center or Not Open at Sufficient Hours',
        'There is no way to meet real locals, the staff constantly channels you away from common people, and lie telling you not associate with locals.',
        'Too far from infrastructure of city',
        'People are too Old to be Fun',
        'Business Center People are not Educated Sufficiently',
        'There is no way to meet real locals, the staff constantly channels you away from common people and lie.',
        'Getting Special Assistants and Language assistants are sub-standard.',
        'The customer is always right is not understood by the local culture.',
        'No Place to Park the Sailboat or Yacht',
        'Concierge Refuses to Arrange for Men or Women Lovers to come to Room',
        'Lockers are Not Secure, and Staff Has Access',
        'Forced to Leave During Day',
        'Drunks Coming in and Out of Dorm',
        'Staff is Indifferent and Non-Caring',
        'Hotel Occupied by One Culture or Country and Dominate',
        'People in the Dorm Havingg Sex',
        'Staff Robs all the Lockers',
        'Staff Robs Backpack Whilee forcing you to Leave for Day',
        'People in Dormitory Rob You',
        'Hours Open is not 24 Hours',
        'Carpet Smells of Cat',
        'Car of Truck Traffic',
        'Receptionist Play Music or do annoying behavior.',
        'Unhelpful staff',
        'Animals, Dog, Cats and Chickens',
        'Construction working being done at hotel or close.',
        'Churches, Mosques Make Noise',
        'No Electricity or Brown Outs',
        'Floor Fan is Missing Plug',
        'Floor Fan is Broken',
        'Fan in Center of Ceiling too Slow',
        'Fan in Center of Ceiling does not Work',
        'Fan in Center of Ceiling only has one speed',
        'Fan in Center of Ceiling Squeaks',
        'Light Bulbs Burned Out',
        'Transom Above Door is Screen and Noise is Loud',
        'Rock and Roll Bands',
        'Staff steals when cleaning the room',
        'Overcharged',
        'Ants',
        'Mosquitoes',
        'No Mosquito Net',
        'Spiders',
        'Mice or Rats',
        'Cockroaches',
        'Screens on Windows to Stop Mosquitoes',
        'Party by Residents in Hotel',
        'Bar in the Hotel Noisy',
        'Plumbing Traps missing on Sink or Shower Drains',
        'Too far from infrastructure of city',
        'Corrugate Tin roofs',
        'Running Vehicles Parked outside of room',
        'There is No Sign to Hang on Door Requesting Room to be Cleaned',
        'No security box big enough for computer or camera.',
        'Courtyard windows facing so you can hear TV, People in other rooms',
        'Tour Buses with Large Groups Making Noise',
        'People Arriving or Leaving Hotel',
        'People coming home after night out',
        'Common Area to close to rooms.',
        'Air Conditioners Blows directly at Bed or Eyes of person sleeping',
        'Air Conditioner is Noisy',
        'Electrical Generator Noise',
        'Hotel Occupied by One Culture or Country and Dominate',
        'Maintenance Never Done',
        'Remote Control on Televisions does not work',
        'No fresh air because of air conditioning and you have sinus or breathing problems.',
        'Group Rents the complete Hotel and makes noise or you have to move.',
        'Ceiling is too High and Air Conditioner does not Cool Room',
        'WIFI or Internet Access only in Common Areas',
        'Toilet Leaking Noise',
        'No Electrical Generator',
        'No booking on arrival or Overbooked',
        'No Prices on Services',
        'Overpriced Phone charges',
        'Mini bar scam',
        'No Business Center',
        'Sex in Next Room',
        'No Health Center or Not Open at Sufficient Hours',
        'No Long Term Storage',
        'No way to wash clothes and none provided',
        'No way to adjust air conditioning',
        'Taxis are Overpriced just outside door to Hotel and no way to get proper priced Taxi',
        'Rooms are not breathing, they are so seal, no fresh air enters, and the new wall air conditioners do not allow.',
        'No Scales to Weigh Luggage',
        'No Closets',
        'No Hangers in Closet',
        'No Shelves',
        'Dirty Hotel',
        'Bums - Beggars Waiting or Hanging out in front of Hotel',
        'Staff Does Not Arrange Taxis',
        'Women are told they cannot be Topless',
        'Tour Sales People Hanging out in front of Hotel',
        'Housecleaning ignores sign and clean room when sign posted to not clean',
        'Common Area Television is Occupied by Soccer of Football Viewers',
        'Failure to Speak English the Language of Business',
        'You assumed more money was better.',
        'Bed Bugs',
        'No Location in the Hotel to Read outside the Room',
        'Poor Room Service',
        'No Common Computer in the Lobby to Check Plane Tickets',
        'Sub Standard restaurant',
        'There is no way to meet real locals, the staff constantly channels you away from common people and lie.',
        'Cancellation costs',
        'Inaccurate Star Rating - (I see this as ludicrous, there is no true standard of Stars for Rooms on the planet, Stars are just an agreed upon Marketing Scheme.)',
        'Business Center People are not Educated Sufficiently',
        'People in Hotel are too young to be Fun',
        'People are too Old to be Fun',
        'No Place to Park the Sailboat or Yacht',
        'Concierge Refuses to Arrange for Men or Women Lovers to come to Room.',
    )
    for index, rule in enumerate(rules):
        issues = randrange(1, 61)
        yield {
            'number': index,
            'description': rule,
            'category': gen_category(),
            'severity': gen_severity(),
            'total_issues': issues,
            'issues': [gen_issue(i) for i in range(1, issues + 1)]
        }


def gen_issue(num):
    return {
        'number': num,
        'where': gen_where(),
        'what': choice(WHAT)
        #'severity': gen_severity()
    }


@app.route('/')
def hello():
    json = dumps({'rules': list(gen_rules())}, indent=True)
    return Response(response=json, status='200', mimetype='application/json')
