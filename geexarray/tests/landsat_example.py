import ee
from geexarray.lib.export_tfrecord_to_GCS import export_to_tfrecord

ee.Initialize()


collection = ee.ImageCollection('LANDSAT/LE07/C01/T1').filterDate('2000-06-01', '2000-06-11')

ETHIOPIA_POLYGON = [[37.93497660463652,8.022690923975954],
                   [39.27530863588652,7.979173384831735],
                   [39.53898051088652,8.261953466694475],
                   [37.97892191713652,8.39239945580339],
                   [37.93497660463652,8.022690923975954]]

ethiopia_polygon = ee.Geometry.Polygon(ETHIOPIA_POLYGON)


collection_to_export = collection.filterBounds(ethiopia_polygon)

export_to_tfrecord(collection_to_export, ethiopia_polygon)