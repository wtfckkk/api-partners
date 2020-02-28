from shapely.geometry import Point, Polygon
from shapely.ops import nearest_points
import math


def get_nearest_partner(partner_queryset, coordinates):
    point = Point(coordinates)
    smallest = None
    for partner in partner_queryset:
        for polygons_coordinates in partner.coverageArea['coordinates']:
            for polygon_coordinates in polygons_coordinates:
                polygon = Polygon(polygon_coordinates)
                p1, p2 = nearest_points(polygon, point)
                distance = math.sqrt(((p1.x - p2.x) ** 2) + ((p1.y - p2.y) ** 2))
                if smallest is None or distance < smallest:
                    smallest = distance
                    nearest_partner_id = partner.id

    return nearest_partner_id
