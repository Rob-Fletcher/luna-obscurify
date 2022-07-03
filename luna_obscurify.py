import argparse
from skyfield.api import load

MOON_RADIUS = 1737400.0  # meters


def get_moon_dist() -> float:
    ts = load.timescale()
    planets = load('de421.bsp')

    Earth, Moon = planets['earth'], planets['moon']
    position = Earth.at(ts.now()).observe(Moon)
    _, _, distance = position.radec()

    return distance.m


def get_object_distance(obj_radius: float = None, avg_moon_dist: bool = True) -> float:
    """Get the distance from the observer the object must be to perfectly obscure the Moon.

    Args:
        obj_radius(float): The radius of the object that should obscure the Moon in meters.
        avg_moon_dist(bool): True; will use the averge distance between Earth and Moon, 
                             False; Uses the skyfield api to calculate the distance using the current date and time.

    Returns:
        The distance from the observer the object must be placed in meters.
    """
    average_moon_dist = 384.4e6  # meters
    if avg_moon_dist:
        moon_dist = average_moon_dist
    else:
        moon_dist = get_moon_dist()
    obj_dist = moon_dist * (obj_radius / MOON_RADIUS)

    return obj_dist


def calculate(obj_diameter: float, use_average: bool) -> float:
    diameter_meters = (float(obj_diameter) / 100.0)  # Convert cm to m
    radius_meters = (diameter_meters / 2.0)  # convert diameter to radius
    dist = get_object_distance(obj_radius=radius_meters, avg_moon_dist=use_average)
    return dist


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--average', '-a', action='store_true', default=False,
                        help="use the average distance between the Earth and Moon.")
    parser.add_argument('--diameter', '-d', type=float, default=None,
                        help="diameter of the object to cover the moon in CM.")
    args = parser.parse_args()

    if args.diameter is None:
        raise ValueError("Must provide object radius with option -d")

    dist = calculate(args)
    print(f"your object should be held at {dist} meters")
