#!/Users/trosine/proj/kerbonauts/env/bin/python
"""List current kerbonauts and their details"""

from operator import itemgetter
import sfsutils

KSP_ROOT = '/Users/trosine/Library/Application Support/Steam/' \
        'steamapps/common/Kerbal Space Program'


def print_kerbal(kerbal):
    """Print out the kerbal's details"""
    kerbal['name'] = kerbal['name'].replace(' Kerman', '')
    form = [
        '{trait:1.1s}',
        '{type:8s}',
        '{state:10s}',
        '{name:15s}',
        '{vessel:20s}',
        '{flags_planted}',
        # '{FLIGHT_LOG}',
        ]
    print(' '.join(form).format(**kerbal))


def assigned_vessels(game):
    """A dict of which vessel each kerbal is assigned to"""
    result = {}
    for vessel in game['GAME']['FLIGHTSTATE']['VESSEL']:
        for part in ensure_list(vessel['PART']):
            for kerbal in ensure_list(part.get('crew', [])):
                result[kerbal] = vessel['name']
    return result


def event_bodies(kerbal, event):
    """Returns a set of bodies where the kerbal has performed an event"""
    bodies = set()

    for log_type in ('CAREER_LOG', 'FLIGHT_LOG'):
        for flight in kerbal[log_type].values():
            for log in ensure_list(flight):
                details = log.split(',')
                if details[0] == event and details[1] != 'Kerbin':
                    bodies.add(details[1])
    return sorted(bodies)


def ensure_list(item):
    """Makes sure that the item is a list"""
    if isinstance(item, list):
        return item
    return [item]


def print_labs(game):
    """List all vessels containing science labs"""
    for vessel in game['GAME']['FLIGHTSTATE']['VESSEL']:
        for part in ensure_list(vessel['PART']):
            if part['name'] == 'Large.Crewed.Lab':
                print(vessel['ORBIT']['REF'], vessel['name'])


def main():
    """List kerbonauts"""
    data = sfsutils.parse_savefile(KSP_ROOT + '/saves/Timmer/persistent.sfs')
    vessel_data = assigned_vessels(data)
    kerbals = data['GAME']['ROSTER']['KERBAL']
    for kerbal in kerbals:
        kerbal['flags_planted'] = event_bodies(kerbal, 'PlantFlag')
        kerbal['vessel'] = vessel_data.get(kerbal['name'], '')

    kerbals = sorted(
        kerbals,
        key=itemgetter('flags_planted', 'state', 'trait', 'name'))
    for kerbal in kerbals:
        if kerbal['type'] not in ('Crew', 'Unowned'):
            continue
        print_kerbal(kerbal)
        # print(kerbal['CAREER_LOG'].keys())
        # break
    print_labs(data)


if __name__ == '__main__':
    main()
