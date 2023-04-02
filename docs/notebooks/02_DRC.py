# # Fixing DRC Errors
#
#

import kfactory as kf

triangle = kf.KCell("triangle")
triangle_poly = kf.kdb.DPolygon(
    [kf.kdb.DPoint(0, 10), kf.kdb.DPoint(30, 10), kf.kdb.DPoint(30, 0)]
)
triangle.shapes(triangle.layer(1, 0)).insert(triangle_poly)
triangle

box = kf.KCell("Box")
box_rect = kf.kdb.DBox(0, 0, 20, 5)
box.shapes(box.klib.layer(1, 0)).insert(box_rect)
box

c = kf.KCell("fix_accute_angle")
c << triangle
c << box
c

c.shapes(c.klib.layer(2, 0)).insert(
    kf.utils.violations.fix_spacing(
        c, 1000, c.klib.layer(1, 0), metrics=kf.kdb.Metrics.Euclidian
    )
)
c
