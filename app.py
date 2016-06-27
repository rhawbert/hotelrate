from json import dumps
from random import choice, randrange

from flask import Flask, Response

app = Flask(__name__)

WHAT = ('Desk', 'Nightstand', 'Minibar', 'Air Conditioner', 'Table', 'Shower', 'Lavatory',
        'Toilet', 'Balcony', 'Window', 'Couch', 'Chair')


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
    where = ('Room', 'Suite', 'Penthouse', 'Hall', 'Lobby', 'Kitchen')
    output = choice(where)
    if output in ('Room', 'Suite', 'Penthouse'):
        number = " {}{:02d}".format(randrange(1, 21), randrange(1, 21))
        output += number
    return output


def gen_rules():
    rules = (
        'Air Conditioner is Noisy',
        'Air Conditioners Blows directly at Bed or Eyes of person sleeping',
        'All debris/trash should be removed from surface',
        'Animals, Dog, Cats and Chickens',
        'Ants',
        'Bar in the Hotel Noisy',
        'Bed Bugs',
        'Bums - Beggars Waiting or Hanging out in front of Hotel',
        'Business Center People are not Educated Sufficiently',
        'Cancellation costs',
        'Car of Truck Traffic',
        'Car, truck taxi, motorcyle noise, and traffic',
        'Carpet Smells of Cat',
        'Cat smells',
        'Ceiling is too High and Air Conditioner does not Cool Room',
        'Churches, Mosques Make Noise',
        'Cockroaches',
        'Common Area Television is Occupied by Soccer of Football Viewers',
        'Common Area to close to rooms',
        'Concierge Refuses to Arrange for Men or Women Lovers to come to Room',
        'Construction for hotel started during high season',
        'Construction project in streets in front of hotel',
        'Construction working being done at hotel or close',
        'Corrugate Tin roofs',
        'Courtyard windows facing so you can hear TV, People in other rooms',
        'Dirty Hotel',
        'Drunks Coming in and Out of Dorm',
        'Electrical Generator Noise',
        'Failure to Speak English the Language of Business',
        'Fan in Center of Ceiling does not Work',
        'Fan in Center of Ceiling only has one speed',
        'Fan in Center of Ceiling Squeaks',
        'Fan in Center of Ceiling too Slow',
        'Floor Fan is Broken',
        'Floor Fan is Missing Plug',
        'Forced to Leave During Day',
        'Furniture is in wrong location',
        'Getting Special Assistants and Language assistants are sub-standard',
        'Group Rents the complete Hotel and makes noise or you have to move',
        'Hotel Occupied by One Culture or Country and Dominate',
        'Hours Open is not 24 Hours',
        'Housecleaning ignores sign and clean room when sign posted to not clean',
        'Housecleaning ignores signs, and clean room when sign posted to not clean',
        'Inaccurate Star Rating',
        'Light Bulbs Burned Out',
        'Lockers are Not Secure, and Staff Has Access',
        'Maintenance Never Done',
        'Mice or Rats',
        'Mini bar scam',
        'Mosquitoes',
        'Never offer to clean the room or change the sheets',
        'No booking on arrival or Overbooked',
        'No Business Center',
        'No Closets',
        'No Common Computer in the Lobby to Check Plane Tickets',
        'No Electrical Generator',
        'No Electricity or Brown Outs',
        'No Electricity or Brown Outs, without generator backup',
        'No fresh air because of type of air conditioning, and you have sinus or breathing problems',
        'No Hangers in Closet',
        'No Health Center or Not Open at Sufficient Hours',
        'No labels on hot or cold water, there is no way to know on or off',
        'No Location in the Hotel to Read outside the Room',
        'No Long Term Storage',
        'No Mosquito Net',
        'No Place to Park the Sailboat or Yacht',
        'No Prices on Services',
        'No Scales to Weigh Luggage',
        'No security box big enough for computer or camera',
        'No Shelves',
        'No way to adjust air conditioning',
        'No way to wash clothes and none provided',
        'Noise coming from plumbing or sanitary pipes as water comes down from upper floors',
        'Overcharged',
        'Overpriced Phone charges',
        'Party by Residents in Hotel',
        'People are too Old to be Fun',
        'People Arriving or Leaving Hotel',
        'People coming home after night out',
        'People in Dormitory Rob You',
        'People in Hotel are too young to be Fun',
        'People in the Dorm Havingg Sex',
        'Permanent sag or dent in mattress',
        'Plumbing Traps missing on Sink or Shower Drains',
        'Poor Room Service',
        'Receptionist Play Music or do annoying behavior',
        'Receptionist playing music or do annoying behavior',
        'Remote Control on Televisions does not work',
        'Rock and Roll Bands',
        'Rooms are not breathing, they are so seal, no fresh air enters, and the new wall air conditioners do not allow',
        'Running Vehicles Parked outside of room',
        'Screens on Windows to Stop Mosquitoes',
        'Sex in Next Room',
        'Spiders',
        'Staff Does Not Arrange Taxis',
        'Staff is indifferent and non-caring',
        'Staff Robs all the Lockers',
        'Staff Robs Backpack Whilee forcing you to Leave for Day',
        'Staff steals when cleaning the room',
        'Sub Standard restaurant',
        'Taxis are Overpriced just outside door to Hotel and no way to get proper priced Taxi',
        'The customer is always right is not understood by the local culture',
        'The Internet is extra charge and the cost is extremely expensive',
        'The problems above, should disappear at higher price levels, or maybe you are paying too much',
        'There is No Sign to Hang on Door Requesting Room to be Cleaned',
        'There is no way to meet real locals, the staff constantly channels you away from common people, and lie telling you not associate with locals',
        'Toilet Leaking Noise',
        'Too far from infrastructure of city',
        'Tour Buses with Large Groups Making Noise',
        'Tour Sales People Hanging out in front of Hotel',
        'Tour sales people hanging, or waiting for you to leave in front of Hotel',
        'Tourist Traps that are too close',
        'Transom Above Door is Screen and Noise is Loud',
        'Unhelpful staff',
        'WIFI or Internet Access only in Common Areas, or you need to pay',
        'Women are told they cannot be Topless',
        'You assumed more money was better',
        'You can hear constructon projects from neighbors',
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
    }


@app.route('/')
def hello():
    json = dumps({'rules': list(gen_rules())}, indent=True)
    return Response(response=json, status='200', mimetype='application/json')
