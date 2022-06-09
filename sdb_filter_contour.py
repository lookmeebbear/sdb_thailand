############################################################
# SIMPLE SATELLITE DERIVED BATHYMETRY THAILAND
# CLEAN SDB RASTER MODEL WITH RASTERIO AND CREATE CONTOUR LINE

import rasterio
import matplotlib.pyplot as plt
from scipy import ndimage, misc
from pathlib import Path
import subprocess as sp
from io import StringIO

print('Open Image and then filter it')
# input image pathname
raster_file = 'depth_kohsamet.tif'

# open image with rasterio and read image
src = rasterio.open(raster_file)
ori_image = src.read(1)

# median filter
mea_image = ndimage.median_filter(ori_image, size=20)

def showsdb(array) :
    plt.rcParams['figure.figsize'] = [18, 15]
    plt.imshow(array,cmap='Spectral',vmin=0, vmax=12)
    plt.colorbar()
    plt.show()
invert_mea_image = (-1)*mea_image
print('check your filtered image before continuing')   
import pdb; pdb.set_trace()

# export image
# Register GDAL format drivers and configuration options with a
# context manager.
print('Export image')
with rasterio.Env():

    # Write an array as a raster band to a new float32 file. For
    # the new file's profile, we start with the profile of the source
    profile = src.profile

    # And then change the band count to 1, set the
    profile.update(
        dtype=rasterio.float32,
        count=1,
        compress='lzw')

    with rasterio.open('depth_filter_kohsamet.tif', 'w', **profile) as dst:
        dst.write(mea_image.astype(rasterio.float32), 1)    # <- Depth for contour production
        
    with rasterio.open('localH_filter_kohsamet.tif', 'w', **profile) as dst:
        dst.write((invert_mea_image).astype(rasterio.float32), 1)   #<- Orthometric Height for profile production

# At the end of the ``with rasterio.Env()`` block, context
# manager exits and all drivers are de-registered.

import pdb; pdb.set_trace()

print('Export utm depth image')
cmd = ''' gdalwarp -s_srs epsg:4326 -t_srs epsg:32647 depth_filter_kohsamet.tif depth_filter_kohsamet32647.tif '''
res = sp.run( cmd, shell=True, capture_output=True )
res = res.stdout.decode('utf-8')

print('Export depth contour')
cmd = ''' gdal_contour -b 1 -a ELEV -i 1.0 -f "GPKG" depth_filter_kohsamet32647.tif contour_1m_kohsamet32647.gpkg '''
res = sp.run( cmd, shell=True, capture_output=True )
res = res.stdout.decode('utf-8')

cmd = ''' gdal_contour -b 1 -a ELEV -i 5.0 -f "GPKG" depth_filter_kohsamet32647.tif contour_5m_kohsamet32647.gpkg '''
res = sp.run( cmd, shell=True, capture_output=True )
res = res.stdout.decode('utf-8')

import pdb; pdb.set_trace()
print('gen contour finish')