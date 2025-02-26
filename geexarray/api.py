import os, sys, time
import ee
sys.path.append(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
)

from google.cloud import storage

from geexarray.lib.export_tfrecord_to_GCS import export_to_tfrecord

# from geexarray.lib.tfrecord_to_xarray import

class GEEXarray:

    def __init__(self, bucket_name="geexarray"):
        # we need gcloud_creds for authenticating to GCS, TODO tell user to specify in docs
        """ Create a new converter """
        self.bucket = bucket_name


    def to_xarray(self, collection, bounds):
        # add the lon-lat information in the export
        collection = collection.map(
            lambda im: im.addBands(ee.Image.pixelLonLat())
        )
        export_to_tfrecord(collection, bounds, self.bucket)
